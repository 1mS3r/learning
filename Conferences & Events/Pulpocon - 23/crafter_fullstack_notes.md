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


## 


### Other Notes

- Scaffolding Testing:
  Unit tests that drive us to create the classes under test and their public methods are called Scaffolding Tests. This particular type of TDD test helps us stay true to the rule that we should not write code unless we have a failing test. Scaffolding tests do not encode expected program behaviour; therefore, we can remove them once they have done their job.