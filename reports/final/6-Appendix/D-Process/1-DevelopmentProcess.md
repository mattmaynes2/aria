# Development Process

## Section goals
- Describe how we started  
- Describe how we work week-to-week
- Problems/Solutions

## Overall Development Plan
---

### Develop product vision
- why are we developing the product?
- what can the product do?

#### Activities
- Use case diagrams
- Scenarios
- SHOULD WRITE DOWN Create a roadmap (how to get to the vision)

## Team Workflow
---
- Iterative approach
- Source code management

### Source Code management

We want to keep track of the historical versions of our source code so that 
we can undo mistakes track how our files have changed over time. We should 
have an "official" version of the current source code, to ensure that our 
code is kept consistent.

We use git because it provides solutions to all of these issues. While several
tools can provide the benefits that we need, git is a familiar choice for all 
team members.

Hosted git server

- in order to allow us to share code easily between different computers, without
maintaining a local git server, we decided to use a hosted git repository. Github
is a free service which allows us to access our code from anywhere, and provides
additional product management services that we make use of.

### Tracking Work

It is important for us to keep an organized list of tasks that need to be completed
for the project, in order for us to gauge the progress of the project and decide 
on which tasks to work on next. 

**Problem**
People don't know what the next thing they should work on is so they don't 
do anything. 

**Solutions**
- Visible list of things to do
- Roughly ordered so that people know what to do next

**Tools that do this**

**Github projects**

- kanban-style board for tracking the status of issues
- doesn't provide an ordered backlog easily
- issues backlog isn't all stuff that we're working on right now
- could use columns in a kanban board to represent priority - easy way to prioritize and sort issues

- We don't want another tool, too many tools is just a pain in the ass
- We don't really care about tracking the status of issues in a sprint, we are only 4 people, this is also 
tracked by issues being opened/closed/assigned

- Branching
- Code reviews

## Testing practices

- TDD
- How are we doing integration testing?
- Continuous integration
