import uuid
from data import *
from valid import *
from tabulate import tabulate





def create_project(user):
    projects = read_projects()

    title = input("Title: ")
    details = input("Details: ")

    try:
        target = input("Total Target (EGP): ")
    except:
        print("Target must be a number")
        return

    start = input("Start Date (YYYY-MM-DD): ")
    end = input("End Date (YYYY-MM-DD): ")

    start_date = valid_date(start)
    end_date = valid_date(end)

    if not start_date or not end_date:
        print("Invalid date format")
        return

    if start_date >= end_date:
        print("End date must be after start date")
        return

    project = {
        "id": str(uuid.uuid4()),
        "user_id": user["id"],  
        "title": title,
        "details": details,
        "target": target,
        "start": start,
        "end": end
    }

    projects.append(project)
    save_projects(projects)

    print("Project created successfully!")



def view_projects():
    projects = read_projects()

    if not projects:
        print("No projects yet")
        return

    table = []
    for p in projects:
        table.append([
            p["id"],
            p["title"],
            p["details"],
            p["target"],
            p["start"],
            p["end"]
        ])

    print(tabulate(table,
                   headers=["ID", "Title", "Details", "Target", "Start", "End"],
                   tablefmt="grid"))



def edit_project(user):
    projects = read_projects()
    project_id = input("Enter project ID: ")

    for p in projects:
        if p["id"] == project_id and p["user_id"] == user["id"]:
            p["title"] = input("New Title: ") or p["title"]
            p["details"] = input("New Details: ") or p["details"]
            p["target"] = input("New Target: ") or p["target"]

            save_projects(projects)
            print("Updated successfully")
            return
    else:
        print("Project not found or not yours")



def delete_project(user):
    projects = read_projects()
    project_id = input("Enter project ID: ")

    new_projects = []

    deleted = False
    for p in projects:
        if p["id"] == project_id and p["user_id"] == user["id"]:
            deleted = True
            continue
        new_projects.append(p)

    if deleted:
        save_projects(new_projects)
        print("Deleted successfully")
    else:
        print("Project not found or not yours")



def search_by_date():
    projects = read_projects()
    date = input("Enter date (YYYY-MM-DD): ")

    results = []
    for p in projects:
        if p["start"] <= date <= p["end"]:
            results.append(p)

    if not results:
        print("No projects found")
        return

    table = []
    for p in results:
        table.append([
            p["title"],
            p["details"],
            p["target"],
            p["start"],
            p["end"]
        ])

    print(tabulate(table,
                   headers=[ "Title", "Details", "Target", "Start", "End"],
                   tablefmt="grid"))
