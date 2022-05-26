def upload_attachments(ticket_id, attachments):

    #Authorization
    username_fh = "#########"
    password_fh = '#########'

    import requests
    url = "REDACTED"
    endpoint_attach = "REDACTED" #AttachFile

    def get_id(link):
        return (link.split("id=",1)[1])

    list_of_files = attachments.split(", ")
    ids_list = list(map(get_id,list_of_files))

    for i in ids_list:
        print("https://drive.google.com/uc?export=download&id=" + i)

    x = 'y'
    local_list_of_files = []
    while x != 'n':
        file_string = input("Input a local list of file names in the Download folder: ")
        local_list_of_files.append(file_string)
        x = input("Do you have another file? Press Enter or n for No: ")

    def post_file(path,id):
        full_path = "REDACTED" + path #Local downloads folder
        file = open(full_path, 'rb')
        files = {
            'file1': file,
        }

        payload_attach = {
            "id": id
        }
        requests.post(f"{url}{endpoint_attach}",auth=(username_fh, password_fh),files=files, data=payload_attach)

    for p in local_list_of_files:
        post_file(p,ticket_id)