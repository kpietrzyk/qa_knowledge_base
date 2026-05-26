#!/usr/bin/env python3
"""
QA Knowledge Base — Tool File Validator
Checks that all tool files contain required sections.
"""

import os
import sys
from pathlib import Path
from typing import NamedTuple

# ANSI colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

REQUIRED_SECTIONS = [
    "## Kategoria",
    "## Do czego służy",
    "## Kiedy używać",
    "## Link",
    "## Prompt AI",
]

RECOMMENDED_SECTIONS = [
    "## Kiedy NIE używać",
    "## Ryzyka i ograniczenia",
    "## Pierwszy praktyczny workflow",
]

class FileResult(NamedTuple):
    path: str
    missing_required: list
    missing_recommended: list
    passed: bool

def validate_file(filepath: Path) -> FileResult:
    content = filepath.read_text(encoding='utf-8')
    missing_required = [s for s in REQUIRED_SECTIONS if s not in content]
    missing_recommended = [s for s in RECOMMENDED_SECTIONS if s not in content]
    return FileResult(
        path=str(filepath),
        missing_required=missing_required,
        missing_recommended=missing_recommended,
        passed=len(missing_required) == 0
    )

def main():
    tools_dir = Path(__file__).parent.parent / "tools"
    if not tools_dir.exists():
        print(f"{RED}Error: tools/ directory not found{RESET}")
        sys.exit(1)

    tool_files = [f for f in tools_dir.rglob("*.md") if f.name != "README.md"]

    if not tool_files:
        print(f"{YELLOW}No tool files found in tools/{RESET}")
        sys.exit(0)

    results = [validate_file(f) for f in sorted(tool_files)]

    passed = [r for r in results if r.passed]
    failed = [r for r in results if not r.passed]
    warned = [r for r in results if r.missing_recommended]

    # Terminal output
    print(f"\n{BOLD}QA Knowledge Base — Tool File Validator{RESET}")
    print("=" * 60)

    for result in results:
        rel_path = result.path.split("tools/")[-1]
        if result.passed:
            status = f"{GREEN}✅ PASS{RESET}"
        else:
            status = f"{RED}❌ FAIL{RESET}"
        print(f"{status} tools/{rel_path}")

        for section in result.missing_required:
            print(f"       {RED}Missing required: {section}{RESET}")
        for section in result.missing_recommended:
            print(f"       {YELLOW}Missing recommended: {section}{RESET}")

    print("\n" + "=" * 60)
    print(f"{BOLD}Summary:{RESET}")
    print(f"  Total files : {len(results)}")
    print(f"  {GREEN}Passed      : {len(passed)}{RESET}")
    print(f"  {RED}Failed      : {len(failed)}{RESET}")
    print(f"  {YELLOW}Warnings    : {len(warned)}{RESET}")

    # Write report
    report_lines = [
        "QA Knowledge Base — Validation Report",
        "=" * 60,
    ]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        report_lines.append(f"{status}: {result.path}")
        for s in result.missing_required:
            report_lines.append(f"  MISSING REQUIRED: {s}")
        for s in result.missing_recommended:
            report_lines.append(f"  MISSING RECOMMENDED: {s}")

    report_lines.append("")
    report_lines.append(f"Total: {len(results)} | Passed: {len(passed)} | Failed: {len(failed)} | Warnings: {len(warned)}")

    report_path = Path(__file__).parent.parent / "validation-report.txt"
    report_path.write_text("\n".join(report_lines), encoding='utf-8')
    print(f"\n  Report saved: validation-report.txt")

    if failed:
        print(f"\n{RED}{BOLD}❌ Validation FAILED — {len(failed)} file(s) missing required sections{RESET}\n")
        sys.exit(1)
    else:
        print(f"\n{GREEN}{BOLD}✅ All tool files passed validation{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
