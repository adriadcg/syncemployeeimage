#!/usr/bin/env python3
import psycopg2 
import paramiko
from configparser import ConfigParser

def config(filename="config.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        config = {p[0]: p[1] for p in params}

    return config


def get_records():
    params = config()
    conn = psycopg2.connect(**params)
    sql = """select res_id, store_fname from ir_attachment 
                where res_model = 'hr.employee' and name ilike 'image_1920' and company_id = 2"""
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    conn.close()

    return records

def move_files(files):
    if len(files) > 0:
        params = config(section="ssh")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(**params)
        paths = config(section="paths")

        general = config(section="general")
        print(general["remote_mode"])
        if general["remote_mode"] == "yes":
            sftp = ssh.open_sftp()
            for f in files:
                from_path = "{}/{}".format(paths["from"], f[1])
                to_path = "{}/{}".format(paths["local"], f[0])
                try:
                    sftp.get(from_path, to_path)
                except Exception as error:
                    print("Error ({}): {}".format(from_path ,error))
            sftp.close()
        else:
            for f in files:
                from_path = "{}/{}".format(paths["from"], f[1])
                to_path = "{}/{}".format(paths["to"], f[0])
                cmd = "yes | cp -f {} {}".format(from_path, to_path)
                print(cmd)
                stdin, stdout, error = ssh.exec_command(cmd)
                # print(stdout.read())
                print(error.read())
        ssh.close()

if __name__ == '__main__':
    records = get_records()
    move_files(records)