# Exercise 8: Creating a Hello World Jenkins Job

## Objective
Create a shell script in GitHub and execute it using a Jenkins Freestyle project.

## Script
The hello-world.sh script prints:
Hello, Jenkins!

## Steps
1. Create a public GitHub repository named devops-sample-code.
2. Add hello-world.sh and push it to the main branch.
3. Open Jenkins at http://localhost:8080.
4. Create a Freestyle project named HelloWorld.
5. Configure Git source control with the repository URL.
6. Add an Execute shell build step:
   sh hello-world.sh
7. Click Build Now.
8. Verify the output in Console Output.

## Expected Result
Hello, Jenkins!
Finished: SUCCESS
