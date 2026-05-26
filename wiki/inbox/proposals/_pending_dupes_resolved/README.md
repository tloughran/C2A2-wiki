# Resolved duplicate proposals

These 36 proposal files were already moved to `approved/` AND copied to `inbox/`
in earlier decision cycles, but their `pending/` copies could not be deleted
because the mounted filesystem blocks `rm` (Operation not permitted).

On 2026-05-24 the daily orchestrator moved them here (mv/rename IS permitted) so
they stop inflating each day's review page. They are the exact contents of
`../_duplicate_pending_to_delete.txt`. Each was verified present in `approved/`
before moving. Safe to delete from a non-mount context; nothing here is awaiting review.
