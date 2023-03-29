## Adding jenkins user to sudoers list 

Jenkins use your VM with user called "jenkins". For the jenkins user to get access to root priveledges we have to give permission that can be similar to super user.

### Step 1: open sudoers file

    sudo vi /etc/sudoers

### Step 2: Add/Modify jenkins user

    jenkins ALL=(ALL) NOPASSWD: ALL

### Step 3: Save and exit vi editor

    Press [ Esc ] and type :wq and hit enter.
