import sched, psutil, time, os, subprocess, docker


event_schedule = sched.scheduler(time.time, time.sleep)

def create_container():
    with open('/etc/haproxy/haproxy.cfg', "r") as f:
        for line in f:
            pass
        last_line = line
    # print(last_line)
    try:
        try:
            port_number = last_line.split('localhost:')[-1]
            new_port = int(port_number) + 1
            print(port_number)
        except:
            port_number = 4999

        new_port = int(port_number) + 1
        print(new_port)
        client = docker.from_env()
        print("running")
        client.containers.run(name=new_port, image="new_flask_app", ports={'5000': new_port}, detach=True)
        with open("/etc/haproxy/haproxy.cfg", "a+") as w:
            w.write(f"    server web{new_port}.example.com localhost:%d\r\n" % (new_port))
        time.sleep(1)
        os.popen("sudo -S %s" % ('service haproxy restart'), 'w').write('Ahmadasad@12506')
        # proxy_rest = subprocess.Popen('sudo service haproxy restart', shell=True)
        # proxy_rest.wait()
        print("done")
    except:
        pass

def delete_container():
    with open('/etc/haproxy/haproxy.cfg', "r") as f:
        for line in f:
            pass
        last_line = line
    f.close()
    print(last_line)
    try:
        port_number = last_line.split('localhost:')[-1]
        print(port_number)
        if int(port_number) > 0:
            print("port greater than 0")
            con_id = subprocess.Popen('docker container rm -f %s' % port_number, shell=True)
            con_id.wait()
            time.sleep(2.4)

            ## Delete last line from file
            print("file deleting")
            with open("/etc/haproxy/haproxy.cfg", "r") as f:
                lines = f.readlines()
            with open("/etc/haproxy/haproxy.cfg", "w") as f:
                for line in lines:
                    if line.strip() != last_line.strip():
                        f.write(line)
        else:
            print("Container not deleted")
        time.sleep(1)
        os.popen("sudo -S %s" % ('service haproxy restart'), 'w').write('Ahmadasad@12506')
        # proxy_rest = subprocess.Popen('sudo service haproxy restart', shell=True)
        # proxy_rest.wait()

    except:
        pass


def check_sys():
    client = docker.from_env()
    cpu_usage = psutil.cpu_percent()
    N = int(cpu_usage / 10)
    print(f"CPU usage: {cpu_usage} Run docker {N} times.")
    # print("CPU usage: ", cpu_usage)

    run_container = client.containers.list()
    print(f"Already Running container: {len(run_container)}")
    running_container = len(run_container)

    # running_container = 2
    # print(f"Already Running container: {running_container}")
    if (N == 0): #need to create 0 container
        if (running_container == 1):  #if running is 1 then pass
            print("pass")
        elif (running_container == 0):  #if running is also 0 then create 1
            print("Need to create 1 container.")
            create_container()
        else:
            print(f"running container {running_container}")
            del_container = running_container - 1
            print(f"Containers need to be deleted {del_container}")
            for d in range(del_container):
                print(d)
                del_container()
    else:
        con_needed = N - running_container
        print(f"Number of container needed: {con_needed}")
        if(con_needed == 0):
            print("pass")
        elif(con_needed > 0):
            print("Addition of containers")
            # add_con = con_needed - running_container
            # add_con = add_con * -1
            add_con = con_needed
            for j in range(add_con):
                print(j)
                create_container()
                # with open('/etc/haproxy/haproxy.cfg', "r") as f:
                #     for line in f:
                #         pass
                #     last_line = line
                # # print(last_line)
                # try:
                #     try:
                #         port_number = last_line.split('localhost:')[-1]
                #         new_port = int(port_number) + 1
                #         print(port_number)
                #     except:
                #         port_number = 4999
                #
                #     new_port = int(port_number) + 1
                #     print(new_port)
                #     client = docker.from_env()
                #     print("running")
                #     client.containers.run(name=new_port, image="new_flask_app", ports={'5000': new_port}, detach=True)
                #     with open("/etc/haproxy/haproxy.cfg", "a+") as w:
                #         w.write(f"    server web{new_port}.example.com localhost:%d\r\n" % (new_port))
                #     os.popen("sudo -S %s" % ('service haproxy restart'), 'w').write('Ahmadasad@12506')
                #     # proxy_rest = subprocess.Popen('sudo service haproxy restart', shell=True)
                #     # proxy_rest.wait()
                #     print("done")
                # except:
                #     pass


            # if (add_con == 0):
            #     for i in range(con_needed):
            #         print(i)
            # else:
            #     for j in range(add_con):
            #         print(j)
        elif(con_needed < 0):
            con_needed = con_needed * -1
            # del_con = running_container - con_needed
            print("Deletion of container")
            for k in range(con_needed):
                print(k)
                delete_container()
                # with open('/etc/haproxy/haproxy.cfg', "r") as f:
                #     for line in f:
                #         pass
                #     last_line = line
                # f.close()
                # print(last_line)
                # try:
                #     port_number = last_line.split('localhost:')[-1]
                #     print(port_number)
                #     if int(port_number) > 0:
                #         print("port greater than 0")
                #         con_id = subprocess.Popen('docker container rm -f %s' % port_number, shell=True)
                #         con_id.wait()
                #         time.sleep(2)
                #
                #         ## Delete last line from file
                #         print("file deleting")
                #         with open("/etc/haproxy/haproxy.cfg", "r") as f:
                #             lines = f.readlines()
                #         with open("/etc/haproxy/haproxy.cfg", "w") as f:
                #             for line in lines:
                #                 if line.strip() != last_line.strip():
                #                     f.write(line)
                #     else:
                #         print("Container not deleted")
                #     os.popen("sudo -S %s" % ('service haproxy restart'), 'w').write('Ahmadasad@12506')
                #     # proxy_rest = subprocess.Popen('sudo service haproxy restart', shell=True)
                #     # proxy_rest.wait()
                #
                # except:
                #     pass


    # if cpu_usage > 10:
    #     N = int(cpu_usage / 10)
    #     print("Opening file")
    #     print(f"CPU usage: {cpu_usage} Run docker {N} times.")
    # else:
    #     print("Keep docker containers to 1")

    event_schedule.enter(15, 1, check_sys, )


e1 = event_schedule.enter(1, 1, check_sys,)
event_schedule.run()




##Working with Flask App
# from flask import Flask
# import socket
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Host Name:  "+ socket.gethostname()+"          My name is Ahmad Asad"
#
#
# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0')


## workign with for loop
# N = 5
# for i in range(N):
#     print(i)




# #Deleting a file
# with open("/etc/haproxy/abc.cfg", "r") as f:
#     lines = f.readlines()
# with open("/etc/haproxy/abc.cfg", "w") as f:
#     for line in lines:
#         if line.strip() != "server web2.example.com localhost:5001":
#             f.write(line)