SELECT * FROM projects;

SELECT * FROM tasks;

SELECT * FROM tasks WHERE status=TRUE;

UPDATE tasks
    SET status = FALSE  
    WHERE id = 2;
    
 DELETE FROM tasks WHERE id=2;
 
SELECT * FROM projects 
JOIN tasks ON tasks.project_id = projects.id