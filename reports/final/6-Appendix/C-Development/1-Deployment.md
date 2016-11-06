### C-1 Deployment {- #C-1-Deployment}

> Author: Matthew Maynes <br/>
> Editors: Cameron Blanchard, Peter Mark <br/>
> Updated: November 6, 2016 <br/>

#### Introduction {-}

This document outlines the details about building and deploying the Aria system. It details how
the system's automated build process executes and the build manifest. This document also outlines the
major decisions that were made to run the build and the reasoning behind them.

#### Build Process {-}

The build process uses a centralized manifest structure to execute the build. The build system does
not use a build automation suite but instead integrates a number of different technologies for
deployment. The executing process that runs the build is a simple shell command executor that
runs over a set of commands from a central manifest.

The central manifest contains all of the build commands for each sub-project. It is a collection
of bash commands that are executed in order to build the system. This manifest file is located
under the build directory and is named `manifest.json`.

The Aria system is composed of many subsystems that each require their own build tool chain. Each
subcomponent has its own set of build commands which are encapsulated within the central manifest.
For this reason, it was decided that a simple command executor would be more suitable for running
the main build process rather then having another architecture to try to execute the commands.

The deployment of the Aria system is not restricted to a single platform but is instead intended to
operate on many different operating systems with many different package managers. To accommodate
this requirement, a package manager wrapper was built. This wrapper dispatches commands to the
appropriate system package manager to download any required dependencies for this project. This
is used in conjunction with the main build system, allowing the Aria system to be deployable on
numerous architectures.

##### Package Management {-}

Almost every system has a different set of package management tools. Most of these tools support the
same features and can access the same packages for their specific system. To enable the Aria system 
to build on independent systems, a package manager wrapper named `pkman` was developed. This wrapper
offers a standard set of package manager commands to install and uninstall packages using the target
platform's specific package manager. This tool uses the facade design technique and allows the build 
process to use one generic interface to communicate to many different dependency management tools.

Since not all platforms offer the same set of packages, a special mode was added to `pkman` to
support optional dependencies. Optional dependencies can be added by specifying a `--try` flag
which indicates that if the package install does not succeed then continue without error. This is
a major improvement that allows us to support packages which have different names per platform or 
even some that only exist on specific platforms.

#### Building Aria {-}

The Aria system is built in several stages. These stages are executed in order to setup the target
system's architecture for running Aria. Each stage is referred to as a directive in the build
process. To perform a complete build these directives must be executed in order and then must be
deployed.

#### Executing a Build {-}

To execute a build in the aria system simple run the `./build/run all` command. This will execute
all of the stages of the Aria build process including the Aria test suite. Once the build has been
successfully built it can be deployed with the `./build/run deploy` command. This will start
the Aria system processes in a daemonized state.

To execute a specific directive in the build, simply run the `./build/run` command with one of
the following directives.

| Directive | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| `enviro`  | Setup the target system's environment dependencies                   |
| `deps`    | Install all of the target specific technologies                      |
| `build`   | Build all of the targets on the build system                         |
| `test`    | Execute the automated test suite on the build                        |
| `deploy`  | Start running the Aria system                                        |
| `clean`   | Clean all of the build artifacts from the repository                 |
| `all`     | Install all of the dependencies, build the system, and run the tests |
