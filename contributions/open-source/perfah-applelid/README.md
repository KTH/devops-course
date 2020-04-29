# Patching wlroots-sys

## Link to repo
Here is a link to the repo where the progress will be made: https://github.com/perfah/wlroots-rs

## Members
1. Per Fahlander (perfah@kth.se)
2. Gunnar Applelid (applelid@kth.se)

## Proposal
Patch the crate [wlroots-sys](https://github.com/swaywm/wlroots-rs/tree/master/wlroots-sys) belonging to the deprecated [wlroots-rs](https://github.com/swaywm/wlroots-rs) (rust bindings for [wlroots](https://github.com/swaywm/wlroots)) library to suit it for use in other projects directly.

A new crate would preferably be published on a separate GitHub repository, although a fork+merge request could also work. The original author would of course be given full credit regardless. 

I think a new repo would be better since I only want to keep the wlroots-sys part of the repo.

Some suggestions for tangible changes to the crate: 

- Make sure that the automatic building work in an self-contained manner as much as possible

- Update the library dependencies to the latest versions

- Refactor deprecated function calls (such as 'bindgen::builder::whitelisted_type(...)')

- Remove references to protocols that no longer exists (such as 'wlroots/protocol/screenshooter.xml')

- Change it so that the building of the crate always is fully self-contained unless explicitly indicated by the user otherwise (maybe)

- Add compilation messages to communicate what  libraries must be installed if some dependency libraries are referenced dynamically

- Make sure that the library's api is sound (exposing the correct data structures)

- Add a README / documentation page


## Motivation

The project was deprecated due to the author giving up on it. There is however interest in the the project (see stars on GitHub) since the project (including it's subcrates) is a useful resource for developing Wayland-compositors in the Rust-language. Patching wlroots-sys would make it possible to interface with the wl-roots c-library directly without dependencies to deprecated bindings.

## Ties to DevOps

The project would involve the following:

- Configure an **automatic building** script for the underlying C-library 

- Configuration of the **packaging** of the library

- Making it as **self-contained** as possible (containerization)


## Context

- Rust: a programming language

- Crate: A packaged library or binary in Rust 

- Wayland-compositor: ~a window manager (usually for Linux)

- wlroots: A library written in C for developing Wayland-compositors

- wlroots-rs: A deprecated library with Rust-bindings for Wlroots. 

- wlroots-sys: A deprecated library within wlroots-rs that offers auto-generation of "raw" bindings from C to Rust.
