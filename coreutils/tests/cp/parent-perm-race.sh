#!/bin/sh
# Make sure cp -pR --parents isn't too generous with parent permissions.

# Copyright (C) 2006-2016 Free Software Foundation, Inc.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

. "${srcdir=.}/tests/init.sh"; path_prepend_ ./src
print_ver_ cp

# cp -p gives ENOTSUP on NFS on Linux 2.6.9 at least
require_local_dir_

umask 002
mkdir mode ownership d || framework_failure_
chmod g+s d 2>/dev/null # The cp test is valid either way.

# Terminate any background cp process
cleanup_() { kill $pid 2>/dev/null && wait $pid; }

for attr in mode ownership
do
  mkfifo_or_skip_ $attr/fifo

  # Copy a fifo's contents.  That way, we can examine d/$attr's
  # state while cp is running.
  cp --preserve=$attr -R --copy-contents --parents $attr d & pid=$!

  (
    # Now 'cp' is reading the fifo.
    # Check the permissions of the temporary destination
    # directory that 'cp' has made.
    ls -ld d/$attr >d/$attr.ls

    # Close the fifo so that "cp" can continue.  But output first,
    # before exiting, otherwise some shells would optimize away the file
    # descriptor that holds the fifo open.
    echo foo
  ) >$attr/fifo

  ls_output=$(cat d/$attr.ls) || fail=1
  case $attr,$ls_output in
  ownership,d???--[-S]--[-S]* | \
  mode,d????-??-?* | \
  mode,d??[-x]?w[-x]?-[-x]* )
    ;;
  *)
    fail=1;;
  esac

  wait $pid || fail=1
done

Exit $fail
