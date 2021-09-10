import os
import subprocess

app_name = 'spb-mtdashboard'

def deploy(app, image, env):
    """Deploy service to cloud run"""
    print("<=============== Deploying to cloud... ========================> \n")

    output = subprocess.run([
        'gcloud', 'run', 'deploy', app,
        '--image', image,
        '--allow-unauthenticated'
        ], shell=True, text=True, stderr=subprocess.STDOUT, env=env)

    print("Completed... \n")

if __name__ == '__main__':
    # ENV VAR
    env = os.environ.copy()
    env['CLOUDSDK_PYTHON'] = 'C:\Program Files\Python38\python.exe'

    deployments = [
            {'app': f'{{app_name}}-frontend', 'image': f'gcr.io/insys-png-ext1/{{app_name}}-frontend'},
            {'app': f'{{app_name}}-backend', 'image': f'gcr.io/insys-png-ext1/{{app_name}}-backend'}
        ]
    
    print("[0] nginx")
    print("[1] frontend")
    print("[2] backend")
    print("[3] deploy all...")

    i = input()
    i = int(i)

    if i == 3:
        for deployment in deployments:
            print("Deploying", deployment['app'], deployment['image'], "...")
            deploy(env=env, **deployment)
    else:
        deployment = deployments[i]
        print("Deploying", deployment['app'], deployment['image'], "...")
        deploy(env=env, **deployment)
    
    print("Done.")


