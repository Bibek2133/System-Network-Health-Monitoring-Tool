# Troubleshooting Guide

## Issue: Application does not start
**Possible Causes**
- Python not installed
- Incorrect Python version
- Script executed from wrong directory

**Resolution Steps**
1. Verify Python installation using `python --version`
2. Ensure Python version is 3.8 or higher
3. Navigate to the correct project directory before execution

## Issue: Case logs are not generated
**Possible Causes**
- File write permission issues
- Application terminated unexpectedly

**Resolution Steps**
1. Run the terminal with appropriate permissions
2. Ensure the application exits gracefully
3. Check available disk space

## Issue: Incorrect priority assigned
**Possible Causes**
- Incorrect diagnostic input
- Misinterpretation of user responses

**Resolution Steps**
1. Re-run diagnostics with accurate inputs
2. Validate issue category selection
3. Review priority scoring logic in code if required

## Issue: Unable to find a previous case
**Possible Causes**
- Incorrect Case ID entered
- Case history file missing

**Resolution Steps**
1. Verify Case ID from logs
2. Ensure `case_history.txt` exists in the project directory
