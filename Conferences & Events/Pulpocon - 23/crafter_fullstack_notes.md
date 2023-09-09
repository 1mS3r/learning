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

### Reading Recommendation

Rompe la barrera del no - Chris Voss

Several techniques to create understanding: Argument summary, last words repetition, ...

### Other Notes

- Scaffolding Testing:
  Unit tests that drive us to create the classes under test and their public methods are called Scaffolding Tests. This particular type of TDD test helps us stay true to the rule that we should not write code unless we have a failing test. Scaffolding tests do not encode expected program behaviour; therefore, we can remove them once they have done their job.