# VASH-2

A refactor of the implementation of the VASH Database System developed for the
Visitor's Aloha Society of Hawaii's (VASH) Big Island branch.
The project was migrated from a LAMP stack to a 100% python 3 code base.
The current implementation is for a single user on their own computer.
The executable will manage a SQLite database for their own reports.
The database should maintain their name, email, and reports.
The executable will be able to manage and merge databases.
In addition generate the monthly/annual report in excel format.

## Dependencies

- python 3
- PySimpleGUI
- SQLite

## How to Build

I assume the target architecture is MacOS.
It would be a good idea to build Windows and Linux binaries as well.

> ```bash
> $ pyinstaller -wF gui.py
> ```

## First Time Start

If no database file is detected run a first time start sequence.
Enter the user's name, email, and default download location into a
SQLite database file.
Load this file and open the Home page

## Home

Contains the following options:

- New Report
- Find Report
- Get Monthly Report
- Get Yearly Report
- Advanced Options
- Settings

### New Report

A form that the user can create a case report and enter some or all information
regarding it.
The user is offered a verification screen before the report is committed to the database.

### Find Report

Allow the user to search on a single field for a report.
Results should be most reverse chronological order.
Results should be clickable and should open the report in full.
The fields will be editable, ideally optionally so.

### Get Monthly Report

Allow the user to download a monthly report from the current year.
The excel report is downloaded to the specified location.
This location can be changed in Settings.

### Get Annual Report

Allow the user to download an annual report from all valid years in the database.
The excel report is downloaded to the specified location.
This location can be changed in Settings.

### Advance Settings

Allow the user to do the following

- Download report for any month
- Download report for custom month ranges
- Merge 2 SQLite databases
- Import excel sheet or database file

### Settings

Allow the user to modifier their name, email settings, and default download location.
