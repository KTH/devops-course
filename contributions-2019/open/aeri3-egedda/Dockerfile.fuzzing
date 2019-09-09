FROM archlinux/base

LABEL maintainer=emil.gedda@emilgedda.se
WORKDIR /

RUN pacman -Syu --noconfirm gcc git make diffutils wget tmux

RUN git clone -j8 https://github.com/mboehme/aflfast.git \
    && cd aflfast && make install -j8

RUN git clone --recurse-submodules -j8 https://github.com/EmilGedda/simdjson.git \
    && cd simdjson \
    && git checkout 7c8404eaf95b2cde087cc131bea42a429fdab8cb \
    && make CXX=afl-g++ allparserscheckfile -j8 \
    && install allparserscheckfile /json-parsers

RUN mkdir -p fuzz/input \
    && cd fuzz/input    \
    && wget https://gist.githubusercontent.com/EmilGedda/370e487cd658b61139b63d92059e73fd/raw/a3b7358f524b9b62af188707c985e8fc586a9997/seed.json


# Set up tmux as two 2x2 windows of AFL fuzzers
CMD tmux -2 new -d -s fuzzer            \
    \; new-window -t fuzzer:1 -n "AFL1" \
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p exploit -M fuzzmaster /json-parsers @@" C-m \
    \; split-window -v                  \                                              
    \; select-pane -t 1                 \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p coe     -S fuzzslave1 /json-parsers @@" C-m \
    \; split-window -h                  \                                              
    \; select-pane -t 2                 \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p coe     -S fuzzslave2 /json-parsers @@" C-m \
    \; split-window -v                  \                                              
    \; select-pane -t 3                 \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p coe     -S fuzzslave3 /json-parsers @@" C-m \
    \; select-layout tile               \                                              
    \; new-window -t fuzzer:2 -n "AFL2" \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p fast    -S fuzzslave4 /json-parsers @@" C-m \
    \; split-window -v                  \                                              
    \; select-pane -t 1                 \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p fast    -S fuzzslave5 /json-parsers @@" C-m \
    \; split-window -h                  \                                              
    \; select-pane -t 2                 \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p fast    -S fuzzslave6 /json-parsers @@" C-m \
    \; split-window -v                  \                                              
    \; select-pane -t 3                 \                                              
    \; send-keys "afl-fuzz -i fuzz/input -o fuzz/output -p explore -S fuzzslave7 /json-parsers @@" C-m \
    \; select-layout tile               \
    \; select-window -t fuzzer:1        \
    \; set-option -g mouse on           \
    \; attach -t fuzzer
