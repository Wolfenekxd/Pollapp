import psycopg2

def election_data(pk):

    conn = psycopg2.connect(dbname="voting_booth", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor.execute('Select a.Answer, a.Result from public.votingbooth_election e join public.votingbooth_answers a on e.id=a.Election_Id_id where a.Election_Id_id = ?', pk)
    data = cursor.fetchall()

    return data

def election_list(pk):

    conn = psycopg2.connect(dbname="voting_booth", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor.execute('Select e.Question, e.Start_date, e.End_date, a.username from public.votingbooth_election e join public.auth_user a on e.Owner_Id_id=a.id where e.id = ?', pk)
    data = cursor.fetchall()


    return data 

