# Assignment Proposal

## Title

Property-based testing with Quickcheck in Haskell

## Names and KTH ID

  - Herdi Saleh (herdi@kth.se)
  - Vincent Lagerros (vinlag@kth.se)

## Deadline

Week 2

## Category

Demo

## Description
The demonstration will begin with a small showcase of property-based testing, which is used
to automate systemic test writing. We will also implement an eDSL (or some sort of custom ADT)
and make it derive the `Arbitrary`  typeclass to allow it to be used for property-based testing within 
the Quickcheck library.

**Relevance**
Property-based testing is used extensively in automated testing. We will specifically demonstrate
how it can be used for custom data types as well, to make it more useful.

Haskell is of specific interest, since most other implementations of property-based testing can
be tracked back to Haskell, and the QuickCheck library.

