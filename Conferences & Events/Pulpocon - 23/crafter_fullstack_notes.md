# Conferences Summary & Notes

## No time to be a Crafter

This is a workshop over trying to refactor and apply clean code practices in a project that was developed with a lot of hurry and is a monoliths with several bad architecture and development decisions.

It was eminently practical but there are some points that can be extracted, thought I can't agree with start the refactor previous to have a proper test battery in place.

### Takeaways Refactor
- Extract logic from big methods into smaller ones
- Each function should have a clear responsibility
- Try to apply [TellDontAsk](https://martinfowler.com/bliki/TellDontAsk.html)
- Avoid starting from Scratch: If not able to have a dedicated team it can be a killer
- Continue to add value: it can, and it should, be intercalated the feature addition with the code refactor
- And this is always a long term job, in my own words `this is not a Sprint but a Marathon`

In the testing part the proposes are esentially aligned with what we are doing at a general level, as workshop was made for Simphony framework there were a bunch of discussion more focused in the technology itself, more than the practises.

### Takeaways Testing
- Esentially the proposes are the same that we follow nowadays.


## Adventurers! To the Train!: The way to go to the data train - Data Driven Orientation

- What's the objetive? -> Generate a good hypothesis
  - Segment Users
  - Impact to achieve
  - Effect of our change
  - Logic that follows previous points
  - Metric to measure

- Define good metrics
  - Comparable: At differents levels, segment users, time period, etc...
  - Understandable: People should be able to discuss about it
  - Behaviour change: What are you going to do if the metric changes

- Data Gathering Quality
  - Establish which data is relevant to avoid having full logs without any meaning
- 
- Experiment before launch
  - Perform several tests: A/B, etc.. to check validity of data aproximation
- 
- Be one with the data
  - Data are not owned by Data team but by ALL the teams

## Vamos a llevarnos bien, porque sino van a haber hondonadas de hostias aqui, eh!

This talk is about Empathy, not false Empathy but real one.
As we are the experts in our area when communicating with a customer, we should have present that there would be a difference in knowledge, that the other part can be nervous and that just our presente works as a balsame, foucs on calls if needed.

- 5 Whys
  - To question why something fail and then why the explanation of that to try to reach root cause
- Dissapooint Early
  - If something feels like a bad idea, say no quick, there is time later to rectify but other way around if more difficult.

### Sensible Customer Meetings
- Establish expectatives beforehand
- Communication with our team mates over customer: Customers come and go, team mates no
- Dont understimate other feelings, even if it feel ilogical or disproportionate
- Dont let an irrelevant discussion deviate you from the original point
- Be honest with customer assuming responsibility
- User the language properly

## Integration first: Building a service with 3rd party integration

After several bad experiences, the development team decided to prioritise the integration with the 3rd party service in their project and, when that is secured, perform several little steps of iteration until project is done, this way avoids last minute integration failures that are painful and unexpècted.

### Reading Recommendation

Rompe la barrera del no - Chris Voss

Several techniques to create understanding: Argument summary, last words repetition, ...

## From programming to develop

Nowadays there are several people that change its carrer path and ends in our field, so, what is our field?

### Artisany
- Well built software
- Deliver value
- Professional communities
- Productive associations

The value in an artisan product is the skill provided when doing the product, lots of times building products which are unique or different from other that fulfills the same purpose.

Another hot point is how the responsibility to transmit our knowledge to new members of the community.

### Design:
- Pass all tests
- Clear code, consistent & expressive
- Avoids duplicity
- Minimum code needed

### Empathy

The purpose, what is the improvement we are going to achieve when doing X task in the life of others?

### Recommended Reading

[10 principios de diseño de Dieter Rams](https://hipertextual.com/2015/01/los-principios-del-buen-diseno-dieter-rams)
[Refactoring](https://www.goodreads.com/book/show/44936.Refactoring?ac=1&from_search=true&qid=sCpLuWGvnq&rank=1)
[Software Economics](https://www.goodreads.com/book/show/59770603-software-economics-una-gu-a-de-estudio)

### Tests

Code with tests is not QA.

- TDD Recommendation
- Especify using examples

### Refactoring

Treat all your code as if it were legacy

#### When to refactor?
- Previous: Code with later refactor in mind os it is easy to modify things.
- Now: Do the change at the moment if its easy
- Later: Modify the code next times so later times are easier to change.

`Adding new features  is important, but refactor the code to allow adding them easily is as important`


## Working with Legacy code

### Sprout method

- Extract the new method/feature to add to legacy code in a new method and then add it to the old code

### Wrap method

- Extract all the old code in a new method, create the method with new logic and mix them in the main method.

### What to look at?
- Code Churn
- Code smell
- Automatic Refactors: Rename, extract variables, inline variable, etc...

### Characterization Testing

https://en.wikipedia.org/wiki/Characterization_test

## Data you don't know you have and how to use it

The mix of psicology and code programming can be taken advantage of -> Behavioural code analysis: How are we interacting with the code?

### GIT / Cloc / CodeMaat

We can retrieve the commits made for each developer, the date, the files involved, ...

- Understand the repo: 
  - Enclosure diagram: size of files plus most edited files or File ownership, which shows who is the one with more changes in a file
  - Change Coupling: Relation between files in the same commits

### Psicology of Code

The different code smells we work to fix have an origin in our own human limitations:
- Short/ work & long place memory, we simply don't have the capacity to work properly with the code if it is not adapted to our capacities

- Onboarding, dont assume the knowledge of the other people
  - Avoid tasks with several stepps of uncertainty: What to change, where to change, how to change, implications...
  - Useful: Take an abstract concept -> go to code to show it -> return to abstract concept and explain other uses

### Resource 

Adam Tornhill - Free graph tool for Open Source project

### Other Notes

- Scaffolding Testing:
  Unit tests that drive us to create the classes under test and their public methods are called Scaffolding Tests. This particular type of TDD test helps us stay true to the rule that we should not write code unless we have a failing test. Scaffolding tests do not encode expected program behaviour; therefore, we can remove them once they have done their job.