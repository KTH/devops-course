# Patching wlroots-sys

## Members
1. Per Fahlander (perfah@kth.se)
2. Gunnar Applelid (applelid@kth.se)

## Links to what we did
[Repository](https://github.com/perfah/wlroots-rs)

[Reflection & Contribution document](https://github.com/perfah/wlroots-rs/wiki/devops-course:-Reflection-&-Contributions)

[Pull request](https://github.com/swaywm/wlroots-rs/pull/300)

[Passing build](https://builds.sr.ht/~timidger/job/214237)

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


### Motivation

The project was deprecated due to the author giving up on it. There is however interest in the the project (see stars on GitHub) since the project (including it's subcrates) is a useful resource for developing Wayland-compositors in the Rust-language. Patching wlroots-sys would make it possible to interface with the wl-roots c-library directly without dependencies to deprecated bindings.

### Ties to DevOps

The project would involve the following:

- Configure an **automatic building** script for the underlying C-library 

- Configuration of the **packaging** of the library

- Making it as **self-contained** as possible (containerization)


### Context

- Rust: a programming language

- Crate: A packaged library or binary in Rust 

- Wayland-compositor: ~a window manager (usually for Linux)

- wlroots: A library written in C for developing Wayland-compositors

- wlroots-rs: A deprecated library with Rust-bindings for Wlroots. 

- wlroots-sys: A deprecated library within wlroots-rs that offers auto-generation of "raw" bindings from C to Rust.


## Project: wlroots-sys

A fork intended for standalone use of the wlroots-sys subcrate (that generates "raw" Rust bindings for [wlroots](https://github.com/swaywm/wlroots) via bindgen). This means that the development is contained only within the [wlroots-sys](https://github.com/perfah/wlroots-rs/tree/master/wlroots-sys) directory. Note that this is not an attempt to revive wlroots-rs - hence the largely untouched repository root. The motivation for this fork is the benefit of being able to write Wayland-compositors based on wlroots in Rust without relying on outdated protocols, dependencies etc.... See below if you are interested in writing one yourself.

### Changes

The following changes have been merged into master:

- Exposed (updated to reflect) all wlr/protocols currently available [here](https://github.com/swaywm/wlroots/tree/master/protocol)
- Exposed (updated to reflect) all wlr/types currently available [here](https://github.com/swaywm/wlroots/tree/master/types)
- Updated all dependencies of wlroots-sys to the current versions (including the library suite “wayland-rs” to >=0.25.*)
- Fixed a bug where wlroots-sys would not compile. The multi-crate issue is described [here](https://users.rust-lang.org/t/unable-to-compile-syntex-syntax-using-rust-1-41/37710).
- Fixed a bug where the wlroots-sys crate would recompile every time you compile another crate that depends on wlroots-sys
- Added informative dependency checks as well as more constructive error messages for pkg-config when building default, static and unstable, for a smoother build process.
- Fixed errors with static build with new version of wlroots.
- Compatibility changes for wlroots-rs (makes CI pass)

### Usage

1. `git clone https://github.com/perfah/wlroots-rs.git`
2. `cd wlroots-rs`
4. `cp ./wlroots-sys <path_to_your_project>/wlroots-sys`
5. Include a crate dependency to your project's `cargo.toml`-file:
        
        [dependencies]
        wlroots-sys = { path = "wlroots-sys", features = [...] }
6. Replace "..." with the optional dependencies you would like.

### Dependencies

- Required dependencies:

        meson
        wayland
        wayland-protocols
        EGL
        GLESv2
        libdrm
        GBM
        libinput
        xkbcommon
        udev 

- Optional dependencies (that can be added as features):   
    - `systemd` - support for logind
    - `elogind` - support for logind without systemd installed
    - `libcap` - capabilities


