from farmsphere.wsgi import application
if __name__=='__main__':
    import uvicorn
    uvicorn.run('farmsphere.wsgi:application', host='0.0.0.0', port=8000)
