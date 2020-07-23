<a href="https://www.arkondata.com/">
    <img src="./img/logo.jpg" align="right" height="80">
</a>

# Arkon's Scala Training

## Description
Scala hands on training project. Looking to introduce new team members or anyone interested to the scala 
programming language and the way it's used within the ArkonData team. 

You'll implement a web server exposing a GraphQL API to expose business retrieved from the INEGI's API and 
query them based on their location.

## Concepts
- FP
    - [Why functional programming?](http://book.realworldhaskell.org/read/why-functional-programming-why-haskell.html)
- Referential transparency.
- Immutability.
- Recursion (FP).
- Basic concurrency using [Scala's Future](https://docs.scala-lang.org/overviews/core/futures.html). 
- Functor/Mondad (FP through [cats](https://typelevel.org/cats/)).
- The real world/side effects using the [IO Monad](http://book.realworldhaskell.org/read/io.html).
- Testing

## Tools
- [Scala](https://www.scala-lang.org/2020/06/29/one-click-install.html)
- [IntelliJ (IDE)](https://www.jetbrains.com/idea/download/)
- [sbt](https://www.scala-sbt.org/)

## Libraries
- [cats](https://typelevel.org/cats/): Library for FP.
- [cats-effect](https://typelevel.org/cats-effect/): IO Monad in Scala.
- [FS2](https://fs2.io/index.html): Functional streams.
- [Doobie](https://tpolecat.github.io/doobie/): Functional layer for JDBC.
- [Sangria](https://sangria-graphql.org/): Scala library for GraphQL.
- [ScalaTest](https://www.scalatest.org/): Scala testing library.
- [ScalaCheck](https://www.scalacheck.org/): Library for random testing of program properties inspired by [QuickCheck](https://hackage.haskell.org/package/QuickCheck).

## Exercises
- [Std lib](https://www.scala-exercises.org/std_lib/asserts)
- [Fp in Scala](https://www.scala-exercises.org/fp_in_scala/getting_started_with_functional_programming)
- [Cats](https://www.scala-exercises.org/cats/semigroup)
- [Circe](https://www.scala-exercises.org/circe/Json)
- [Doobie](https://www.scala-exercises.org/doobie/connecting_to_database)
- [ScalaCheck](https://www.scala-exercises.org/scalacheck/properties)

## Basic commands
SBT console
```
$ sbt
```

Running sbt commands inside the SBT console
```
// sbt console
$ sbt

// Scala REPL
$ sbt console

// Compile the main module
sbt:arkon-scalatraining> compile

// Compile the test module
sbt:arkon-scalatraining> test:compile

// Run all tests
sbt:arkon-scalatraining> test

// Run a specific test
sbt:arkon-scalatraining> testOnly training.std.OptionSpec
```

## Requirements
- web service
- 
