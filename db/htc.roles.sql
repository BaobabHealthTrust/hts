INSERT INTO role (role, description, uuid) VALUES ("Counselor", "HTS Counselor role", (SELECT UUID())), ("HTS Focal Person", "HTS Clinic Supervisor role", (SELECT UUID())), ("Admin", "HTS System Administrator role", (SELECT UUID()))
