# What makes a good test suite?

## Code coverage

* Purpose

    - Check how production code has been executed by tests

* Pros

    - Automated

    - Fast

    - Code not covered $\implies$ code not tested

* Cons

    - Code covered $\not \Rightarrow$ code tested

    - False sense of security?

## Mutation testing

* Purpose

    - Check if tests observe incorrect states

* Pros

    - Indicates what has not been tested properly

    - Automated

* Cons

    - Traditional mutation testing takes a _long_ time [@niedermayr2016will]

    - Equivalent mutants (8-9% [@offutt1997automatically;@bybro2003mutation]) 

## Maintainability

* Performance measures exclusively focused on _now_

* Software maintenance costs typically exceed 50% of total cost [@hunt2008software;@labuschagne2017measuring;@alegroth2016maintenance]

* Performance now $\not \Rightarrow$ performance tomorrow

    - ABB test suite started at 90% coverage

    - Ten years later: 10% coverage, rarely even run [@robinson2011scaling]

## A maintainable test case


> "[...], a good test case should not only be sensitive to deviations from
> the intended behavior, but should also be maintainable in its own right;
> **it should be easy to understand so that it can be readily adapted to changes in
> the rest of the code base as it evolves.**" [@shamshiri2018automatically]

* DevOps is heavily focused around software as a living thing

# Are automatically generated tests "good" tests?

## Fibo.java

```java
public class Fibo {
    private long current;
    private long next;

    public Fibo() {
        current = 0;
        next = 1;
    }

    public long next() {
        long previous = current;
        current = next;
        next = previous + current;
        return previous;
    }
}
```

## EVOSUITE generated test

```java
@Test(timeout = 4000)
public void test0()  throws Throwable  {
  Fibo fibo0 = new Fibo();
  long long0 = fibo0.next();
  assertEquals(0L, long0);
  
  long long1 = fibo0.next();
  assertEquals(1L, long1);
}
```

### Clean test?
1. Tests one thing?
2. Good test name?
3. Clear structure (e.g. AAA)?


## Not a very good test suite

* Assumes current implementation is correct
    
    - To us, testing should be about contesting correctness

* Test scores high on performance (full coverage, 71%
  mutation score)

    - But would pass a function generating 0, 1, 2...

* Test has no obvious purpose

    - Harder for human testers to understand and maintain [@shamshiri2018automatically;@honfi2017classifying]

# Summary and references

## Takeaways

* Performance is _hard_ to measure in a general way

* High performance $\not \Rightarrow$ good test suite

    - Maintainability is also important

* AGTs do what they are designed to do well

    - But the design is flawed


## References {.allowframebreaks} 
