 openapi: 3.0.3
 info:
    title: jobs_projects_user_api
    description: An API contract with endpoints to get, insert and update jobs, projects and users associated to that
    version: 1.0

servers:
    url: https://api.jobs.com/v1
    description: url to hit the API endpoints

paths:
    /health
        get:
            summary: Check API health
            Id: getHealth
            idempotency: true

    /users
            get:
            summary: To get all users
            Id: getUsers
            idempotency: true
            description: list all users
            paramters:
                limit:20
                cursor
          responses:
            "200":
            description: A list of users
            content:
                application/json:
                schema:
                    type: array
                    items:
                    $ref: "#/components/schemas/User"
            "404":
                description: User not found
        post:
            summary: Create a new user
            Id: addUsers
            idempotency: false
            description: Add a new user to the DB server
            requestBody:
                required:true
                content:
                    application/json: createUserRequest
            responses:
                "201":
                description: User created successfully
                content:
                    application/json:
                    schema:
                        $ref: "#/components/schemas/User"

    /users/{userid}:
        get:
            summary: To get users by userID
            Id: getUsers
            idempotency: true
            description: get one user based on userID
            paramters:
                userid
                limit:20
                cursor
          responses:
            "200":
            description: A list of users
            content:
                application/json:
                schema:
                    type: array
                    items:
                    $ref: "#/components/schemas/User"
            "404":
                description: User not found

        patch:
            summary: Update user address
            Id: updateNewAddress
            idempotency: True
            description: Update the address feild with new address in user details
            requestBody:
                required:true
                content:
                    application/json: updateUserRequest
            parameters:
                userid

    /jobs
        get:
            summary: To get list of jobs active
            Id: listJobs
            idempotency: true
            description: list of active jobs
            paramters:
                status
                limit:20
                cursor
          responses:
            "200":
            description: A list of jobs
            content:
                application/json:
                schema:
                    type: array
                    items:
                    $ref: "#/components/schemas/jobs"
            "404":
                description: Jobs not found
        post:
            summary: Create a new job
            Id: addJobs
            idempotency: false
            description: Add a new job to the DB server
            requestBody:
                required:true
                content:
                    application/json: createJobRequest
            responses:
                "201":
                description: Job created successfully
                content:
                    application/json:
                    schema:
                        $ref: "#/components/schemas/Job"


    /jobs/{job_id}
        get:
            summary: To get list of jobs active
            Id: listJobs
            idempotency: true
            description: list of active jobs
            paramters:
                job_id
                status
                limit:20
                cursor
          responses:
            "200":
            description: A list of jobs
            content:
                application/json:
                schema:
                    type: array
                    items:
                    $ref: "#/components/schemas/jobs"
            "404":
                description: Jobs not found
 
        patch:
            summary: Update status of job by job id
            Id: updateJobStatus
            idempotency: True
            description: Update the Job status of the job
            requestBody:
                required:true
                content:
                    application/json: updateJobStatusRequest
            parameters:
                job_id     
        put:
            summary: Update the job with new details
            Id: updateJobDetails
            idempotency: True
            description: Update the Job details
            requestBody:
                required:true
                content:
                    application/json: updateJobRequest
            parameters:
                job_id 
        delete:
            summary: delete the existing job with job_id
            Id: deleteJobDetails
            idempotency: True
            description: Delete the Job details
            parameters:
                job_id 

    /projects
        get:
            summary: To get list of active projects 
            Id: listProjects
            idempotency: true
            description: list of active projects
            paramters:
                status
                limit:20
                cursor
          responses:
            "200":
            description: A list of projects
            content:
                application/json:
                schema:
                    type: array
                    items:
                    $ref: "#/components/schemas/projects"
            "404":
                description: project not found
        post:
            summary: Create a new project
            Id: addproject
            idempotency: false
            description: Add a new project to the DB server
            requestBody:
                required:true
                content:
                    application/json: createProjectRequest
            responses:
                "201":
                description: Project created successfully
                content:
                    application/json:
                    schema:
                        $ref: "#/components/schemas/Project"

    /projects/{project_id}
        get:
            summary: To get list of active projects 
            Id: listProjects
            idempotency: true
            description: list of active projects
            paramters:
                project_id
                status
                limit:20
                cursor
          responses:
            "200":
            description: A list of projects
            content:
                application/json:
                schema:
                    type: array
                    items:
                    $ref: "#/components/schemas/projects"
            "404":
                description: project not found
 
        patch:
            summary: Update status of project by project id
            Id: updateProjectStatus
            idempotency: True
            description: Update the status of the project
            requestBody:
                required:true
                content:
                    application/json: updateprojectStatusRequest
            parameters:
                project_id     
        put:
            summary: Update the project with new details
            Id: updateProjectDetails
            idempotency: True
            description: Update the project details
            requestBody:
                required:true
                content:
                    application/json: updateProjectRequest
            parameters:
                project_id        

