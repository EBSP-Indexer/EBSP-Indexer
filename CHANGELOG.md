
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [Unreleased] - yyyy-mm-dd
 
Here we write upgrading notes for brands. It's a team effort to make them as
straightforward as possible.
 
### Added
- [PROJECTNAME-XXXX](http://tickets.projectname.com/browse/PROJECTNAME-XXXX)
  MINOR Ticket title goes here.
- [PROJECTNAME-YYYY](http://tickets.projectname.com/browse/PROJECTNAME-YYYY)
  PATCH Ticket title goes here.
 
### Changed
 
### Fixed
 
## [0.2.0] - 2024-03-???
  
TODO: Here we would have the update steps for 1.2.4 for people to follow.
 
### Added
- "Help" menu that includes information about the software, authors, and dependency versions that are of importance to the user. The menu also includes navigation to EBSP Indexer on GitHub and Zenodo.
- Ability to perform Hough Indexing using more than two phases, regardless of whether or not the phase has a cubic crystal system.
- More default options for indexing in the settings dialog
- A changelog.

### Changed
  
- Increase versions of kikuchipy, PyEBSDIndex and diffsims to 0.9.0, 0.2.0, and 0.5.2, respectively. ([#168](https://github.com/EBSP-Indexer/EBSP-Indexer/pull/168))
- Use kikuchipy's imaging module to replace its deprecated generators module. 
- Set pyinstaller requirement to a fixed version (5.10.1) instead of using latest development build.

### Removed
- Restrictions in Hough Indexing dialog related to adding phases and create a phase map
 
### Fixed
- System Viewer showing a file is selected after returning from the settings window, even though it is not. 
- Refinement of orientations of a crystal map which includes not_indexed points, might produce results that cannot be opened in signal navigation. ([#168](https://github.com/EBSP-Indexer/EBSP-Indexer/pull/168))