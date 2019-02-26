# File Shuttling (with some bugs :))

For this project, we've created a super simplified version of what our data integration with clients looks like.  Right now, it has some bugs in it.  Your task is to fix those bugs.  

## Goal:

Here is what the system should do:
1) A user uploads file onto SFTP Server
2) This triggers an `HTTP POST /upload` call to a flask api
3) The flask application writes the file to `s3`

## Infrastructure description
 * SFTP EC2 instance:
   ```
   Instance ID: i-0948c0221c97039a4
   Public IP: 34.219.141.195
   SSH: ssh ubuntu@34.219.141.195
   ```
   *Description*:
     This server is an SFTP server.  A user can connect to it by running:
   `sftp hello@34.219.141.195`
   They can then upload files into the `here` directory.  

   *Processes running*:
   `sudo -E nohup bash watch_dir.sh &`                 
     This process watches for new files.  Whenever a new file is added to the directory `home/hello/here`, it kicks off the `/home/ubuntu/shuttle.py` script.  
 * Flask EC2 instance:
   ```
   Instance ID: i-0948c0221c97039a4
   Public IP: 34.219.141.195
   SSH: ssh ubuntu@34.219.141.195
   ```
   *Description*:
     This is a server running a docker container that serves a Flask 
      application.  
   *Processes running*:
   `sudo docker run -d flask_api:latest python3 app.py`

