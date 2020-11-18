import psycopg2

def election_data(election_id):

    conn = psycopg2.connect(dbname="voting_booth", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor.execute("Select a.Answer, a.Result from public.votingbooth_election e join public.votingbooth_answers a on e.id=a.Election_Id_id where a.Election_Id_id = ?;", election_id)
    data = cursor.fetchall()

    return data