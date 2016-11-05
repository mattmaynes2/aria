### Development Process

#### Introduction {-}
An important part of any sizeable software project is the selection of a development process.
A development process imposes a particular structure on the development of a product. The 
process used for the development of this project was created with the following factors in mind:

- Project lifespan: Work on the project will last at least 8 months; other developers may also
continue working on the project after the two school terms are complete

- Team Size: There are four team members working on the project, the process needs to keep everyone 
synchronized and organize the assignment of work to team members

- Reporting: The final project report critical to the project's success, the process should make the report easy to write

- Code Quality: The process should ensure that work products are of the quality expected of a fourth year project.

- Maintainability and Extensibility: The end result of the project should be maintainable and extensible; a developer 
who is new to the project should have an easy time developing for it.

- Ease of Implementation: The process should not be an obstacle to development

Given these goals, the process used for this project incorporates some elements of Extreme Programming and other
agile methodologies. Use of practices which are widely accepted in industry also ensures that new developers are 
comfortable working on the project. The process prescribes some practices to be used for: Source code management, 
Code reviews, Issue Tracking, and Testing.

##### Source Code Management {-}

The project uses a source code management tool to achieve the following goals:

- Allows many team members to work on the same codebase and maintain a consistent master copy of the product

- Track changes to files in order to locate changes that may have introduced bugs

- Allows team members to work independently

This project uses git because it provides solutions to all of these issues. git is familiar to all 
team members, in addition to being a de-facto standard in the open source software community.
Using git over other SCM tools makes the process easier to follow, and improvse the experience of any
new developer that might choose to maintain the project. 

The project's git repository is hosted on Github. Github allows the team to access the project anywhere,
and makes sharing code with new developers very simple. Additionally, Github provides some project management 
tools that can be used elsewhere in the process, as explained in subsequent sections.

##### Branching and Code Reviews {-}

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

##### Continuous Integration {-}

A practice which complements the branching strategy adopted by this project is Continuous Integration. 
In combination with test automation, Continuous Integration allows team members to get early 
feedback about changes they make to the codebase. Proper use of Continuous Integration can ensure
that the project's master copy remains in a working state at all times. One of the benefits of maintaining
working sofware at all times is that the project is always demoable.

The continuous integration tool chosen for this project is Travis CI. Travis CI is a free hosted CI system.
Travis can be easily integrated with Github repositories, making it the obvious choice for this project.

##### Issue Tracking {-}

It is important for us to keep an organized list of tasks that need to be completed
for the project, in order for us to gauge the progress of the project and decide 
on which tasks to work on next. In addition, reporting on the progress of the project, as well
as generation of the final report, will be easier given a list of the tasks that were completed.
Another aspect of tracking work is coordinating people (deciding who is working on what)

- Visible list of things to do
- Roughly ordered so that people know what to do next
- Provides a forum for discussion of tasks


TODO
## Testing practices

- TDD
- How are we doing integration testing?

#### Overall Development {-}

##### Develop product requirements {-}
- why are we developing the product?
- what can the product do?

##### Activities {-}
- Use case diagrams
- Scenarios
- SHOULD WRITE DOWN Create a roadmap (how to get to the vision)
