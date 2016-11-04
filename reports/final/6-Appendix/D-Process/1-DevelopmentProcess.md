### Development Process

#### Introduction {-}

##### What is a process? {-}
- imposition of a structure to development

##### Why do we need a process? {-}
- project has a long lifespan (8 months)
- 4 people working on it, we need to keep everyone synchronized
- we have some specific deadlines that we need to hit
- reporting is critical, we need to ensure that our goals are clearly defined, and that work
toward them is tracked so that it's easier to write about
- our process should also ensure that code is of the quality expected of a fourth year project

##### Considerations in in process creation {-}
- team size (the team is small, 4 people)
- lifetime of project (someone should be able to pick it up after we finish)
- it should be easy to follow, not an obstacle

#### Overall Development {-}

##### Develop product requirements {-}
- why are we developing the product?
- what can the product do?

##### Activities {-}
- Use case diagrams
- Scenarios
- SHOULD WRITE DOWN Create a roadmap (how to get to the vision)

##### Team Workflow {-}
- Iterative approach
- Source code management

#### Tools {-}

##### Source Code management {-}

- We have multiple people working on the same code, we need to maintain a version of the software 
that is in a consistent state
- We want to be able to track changes to files so that we can undo them if necessary, and get hints 
 about what changes introduced problems
- Allows people to work independently on a set of files and merge them together 

We use git because it provides solutions to all of these issues. While several
tools can provide the benefits that we need, git is a familiar choice for all 
team members, in addition to being a de-facto standard in the open source software community.
This makes the process easier to follow, and potentially makes it easier for other developers
to pick up the project when we are done with it

Hosted git server

- using a hosted git server allows us to access our code anywhere

- makes sharing with other developers easy

Github is a free hosting service for git repositories. It is well known in the development 
community, and accomplishes both of the goals stated above. Additionally, it provides some
project management tools that we can used, as explained in subsequent sections.

##### Branching and Code Reviews

We make strategic use of a git feature, branching, in order to ensure that code which makes it into the
official version of our software is of the quality expected of a fourth year project. A technique we are
using to ensure code quality is peer code review. By frequently reviewing code, we can share knowledge 
between team members with different amounts of experience in particular technologies. 

In order for code reviews to be effective, we believe that the review should be as short as possible,
and focused on a particular feature. This ensures that reviewers are motivated to provide high quality 
feedback. In order to encourage this, we have adopted a the "feature branches" branching strategy. Work on
a particular feature is submitted to its own branch; branches are merged to master once work on the 
feature has been completed. A code review is required before any branch may be merged into master. Feature 
branches helps to ensure that code reviews are short and focused.

An additional benefit of the feature branching strategy is that it encourages frequent integration of 
the system's components. 

##### Continuous Integration

- we want to find problems as soon as possible
- we want to get features working quickly

##### Tracking Work {-}

It is important for us to keep an organized list of tasks that need to be completed
for the project, in order for us to gauge the progress of the project and decide 
on which tasks to work on next. In addition, reporting on the progress of the project, as well
as generation of the final report, will be easier given a list of the tasks that were completed.
Another aspect of tracking work is coordinating people (deciding who is working on what)

- Visible list of things to do
- Roughly ordered so that people know what to do next
- Provides a forum for discussion of tasks

##### Tools

##### Github

- provides issue tracking software
- prioritization of issues using tags
- organization of issues into milestones
- assign people to issues
- a tool which we are already using in our project!

## Testing practices

- TDD
- How are we doing integration testing?
- Continuous integration
