#!/usr/bin/env python3
"""
append_decision_email.py — idempotently append one [C2A2-review-decision] email
to provenance/decision_emails.json (the Review Log response side).

Called by the daily review agent in Phase 0, once per decision email processed.
Idempotent on thread_id: re-running with the same email is a no-op.

Usage:
  python3 append_decision_email.py --json provenance/decision_emails.json \
     --thread <id> --message <id> --date <ISO> \
     --subject "<subject>" --sender "<addr>" --labels "SENT,INBOX" \
     --bodyfile /tmp/body.txt
  (body may instead be piped on stdin)
"""
import sys, os, json, argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True)
    ap.add_argument("--thread", required=True)
    ap.add_argument("--message", default="")
    ap.add_argument("--date", required=True)
    ap.add_argument("--subject", default="")
    ap.add_argument("--sender", default="")
    ap.add_argument("--labels", default="")
    ap.add_argument("--bodyfile", default="")
    args = ap.parse_args()

    body = open(args.bodyfile, encoding="utf-8").read() if args.bodyfile else sys.stdin.read()

    if os.path.exists(args.json):
        data = json.load(open(args.json, encoding="utf-8"))
    else:
        data = {"_note": "Verbatim [C2A2-review-decision] emails (response side of the Review Log).",
                "emails": [], "_resend_threads": []}
    data.setdefault("emails", [])

    if any(e.get("thread_id") == args.thread for e in data["emails"]):
        print("noop: thread %s already present" % args.thread)
        return

    data["emails"].append({
        "thread_id": args.thread, "message_id": args.message, "date": args.date,
        "subject": args.subject, "sender": args.sender,
        "labels": [s for s in args.labels.split(",") if s], "body": body.strip()})
    data["emails"].sort(key=lambda e: e.get("date", ""))
    json.dump(data, open(args.json, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("appended: %s (%s) -> %d emails" % (args.subject, args.date, len(data["emails"])))


if __name__ == "__main__":
    main()
