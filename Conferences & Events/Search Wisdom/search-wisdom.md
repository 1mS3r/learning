# Search Wisdom by OpenSource Connections

## Structuring Teams - Team Topologies

An optimized team structure will affect even the system design outcome, we can't attach to a single pattern that works in every case, it will depend on the organization and product.

We should:
 - Avoid feature teams
 - Build a stream in which development flows: Frontend -> Backend -> DB

### Cognitive Load & Comm Patterns

Its fundamental to make an effor to reduce cognitive load (amount of mental effort used)
    - Intrinsic: fundamental problems -> structuring a Java class
    - Extraneous: How to deploy a compoenent? How to connect to X service?
    - Germane: Specific aspects which need to be learned -> Business domain, new tech advancements

A high number of communication patterns is the ideal within a team lessening the points of communication when reaching outsidethe team.
Try to keep the teams following the 2 pizza rule ([copied of Jeff Bezo's](https://www.theguardian.com/technology/2018/apr/24/the-two-pizza-rule-and-the-secret-of-amazons-success))

### Team Types

#### Team Topologies

dasd

## Vector Search

### How to combine

The best approach from a findability/relevancy perspective is to add the particular term to the generated vector, generated vectors are dependant on the generating strategy followed, eg. nDCG@30, P@30,...

### Score combination

- Sum of scores: Cosine Similarity + BM25
- RRF (Reciprocal Rank Fusion): 1/k+rank(keyword)

## Querqy Library

Library for query rewriting available in several search systems such as: opensearch, elasticsearch, Solr, ...

