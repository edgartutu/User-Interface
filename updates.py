from database import db,Medicine,Phone

x = Medicine('pan','1234567','12/1/2020','12345')
db.session.add_all([x])
db.session.commit()
print(x)
