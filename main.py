#!/usr/bin/env python3
"""One code review comment: approve the pull request, quietly dread everything.

Writes the comment to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to
/output/entry.txt when the variable is unset.
"""

from pathlib import Path
import os

comment = "LGTM — I understood roughly none of this, but the tests pass, and the sun will rise anyway."

destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
destination.mkdir(parents=True, exist_ok=True)
(destination / "entry.txt").write_text(comment, encoding="utf-8")
