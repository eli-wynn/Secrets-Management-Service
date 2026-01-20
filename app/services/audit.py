from app.db.models import AuditLog

def log_action(db, user_id, action, secret_id):
    entry = AuditLog(
        user_id=user_id,
        action=action,
        secret_id=secret_id
    )
    db.add(entry)
    db.commit()
