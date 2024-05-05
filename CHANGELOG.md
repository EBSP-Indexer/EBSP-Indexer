
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.2.0] - 2024-05-05
  
A new Windows installer for version 0.2.0 can be found here:
TODO

There does not exist a macOS application of v0.2.0 as of now.

### Known issues
- Inspecting geometrical simulations of non-cubic crystal maps (e.g. hexogonal) using signal navigation is not properly supported, and may only show one or two bands.
 
### Added
- "Help" menu that includes information about the software, authors, and dependency versions that are of importance to the user. The menu also includes navigation to EBSP Indexer on GitHub and Zenodo.
- Ability to perform Hough Indexing using more than two phases, regardless of whether or not the phase has a cubic crystal system.
- More default options for indexing in the settings dialog
- A changelog.

### Changed
- Increase versions of kikuchipy, PyEBSDIndex and diffsims to 0.9.0, 0.2.0, and 0.5.2, respectively. ([#168](https://github.com/EBSP-Indexer/EBSP-Indexer/pull/168))
- Use kikuchipy's imaging module to replace its deprecated generators module. 
- Set pyinstaller requirement to a fixed version (5.10.1) instead of using latest development build.
- Decrease the size of legends and scalebars in IPF and phase maps from indexing and refinement.

### Removed
- Restrictions in Hough Indexing dialog related to adding phases and create a phase map
 
### Fixed
- Issue when loading master patterns where the name of phase contains slashes (e.g. a system path).
- Properties disappearing from project_settings.txt
- System Viewer showing a file is selected after returning from the settings window, even though it is not. 
- Refinement of orientations of a crystal map which includes not_indexed points, might produce results that cannot be opened in signal navigation. ([#168](https://github.com/EBSP-Indexer/EBSP-Indexer/pull/168))