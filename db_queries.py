#!/usr/bin/python

import psycopg2
from config import config
from datetime import datetime, date


def search_patient(username, password):
    signed_up = 0
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT username, password FROM patient where username=%s and password=%s;"
        cur.execute(sql, (username, password))
        
        if cur.rowcount > 0:
            signed_up = 1
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return signed_up


def get_patient_details(username):
    conn = None
    details = dict()
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT * FROM patient where username=%s;"
        cur.execute(sql, (username,))
        
        rv = cur.fetchone()
        details['patient_id'] = rv[0]
        details['username'] = rv[1]
        details['name'] = rv[2]
        details['email'] = rv[3]
        details['password'] = rv[4]
        details['mobile'] = rv[5]
        details['age'] = rv[6]
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return details


def get_patient_name(patient_id):
    name = ""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT name FROM patient where patient_id=%s;"
        cur.execute(sql, (patient_id, ))
        
        name = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return name


def get_patient_id(username):
    id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT patient_id FROM patient where username=%s;"
        cur.execute(sql, (username, ))
        
        id = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def search_doctor(username, password):
    signed_up = 0
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT username, password FROM doctor where username=%s and password=%s;"
        cur.execute(sql, (username, password))
        
        if cur.rowcount > 0:
            signed_up = 1
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return signed_up


def get_doctor_details(username):
    conn = None
    details = dict()
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT * FROM doctor where username=%s;"
        cur.execute(sql, (username,))
        
        rv = cur.fetchone()

        details['doctor_id'] = rv[0]
        details['username'] = rv[1]
        details['name'] = rv[2]
        details['email'] = rv[3]
        details['password'] = rv[4]
        details['mobile'] = rv[5]
        details['age'] = rv[6]
        details['experience'] = rv[7]
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return details


def get_doctor_qualifications(username):
    conn = None
    quals = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        docid = get_doctor_id(username)

        sql = """
        SELECT qf.qual_name, qd.procurement_year, qd.institute FROM qualified qd
        left join qualification qf on qd.qual_id=qf.qual_id
        where qd.doctor_id=%s;
        """
        cur.execute(sql, (docid,))
        
        for i in range(cur.rowcount):
            quals.append(cur.fetchone())
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return quals


def get_doctor_name(doctor_id):
    name = ""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT name FROM doctor where doctor_id=%s;"
        cur.execute(sql, (doctor_id, ))
        
        name = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return name


def get_doctor_id(username):
    id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT doctor_id FROM doctor where username=%s;"
        cur.execute(sql, (username, ))
        
        id = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def search_username(username):
    signed_up = 0
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT username, password FROM patient where username=%s;"
        cur.execute(sql, (username,))
        
        if cur.rowcount > 0:
            signed_up = 1

        sql = "SELECT username, password FROM doctor where username=%s;"
        cur.execute(sql, (username,))

        if cur.rowcount > 0:
            signed_up = 1
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return signed_up


def get_all_specs():
    specs = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT speciality FROM specialization;"
        cur.execute(sql)

        for i in range(cur.rowcount):
            specs.append(cur.fetchone()[0])      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return specs


def get_spec_id(speciality):
    spec_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT spec_id FROM specialization where speciality=%s;"
        cur.execute(sql, (speciality,))
        spec_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return spec_id


def get_slot_id(slot):
    slot_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT slot_id FROM slots where start_time=%s and end_time=%s;"
        cur.execute(sql, (slot[0],slot[1]))
        slot_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return slot_id


def get_doctor_slots(doctor_id):
    slots = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
        SELECT s.start_time, s.end_time FROM has_slots hs
        left join slots s on hs.slot_id=s.slot_id
        where hs.doctor_id=%s;
         """
        cur.execute(sql, (doctor_id,))

        for i in range(cur.rowcount):
            slots.append(cur.fetchone())    
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return slots


def get_doctor_specs(doctor_id):
    specs = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
        SELECT sn.speciality FROM specialized s
        left join specialization sn on s.spec_id=sn.spec_id
        where s.doctor_id=%s;
         """
        cur.execute(sql, (doctor_id,))

        for i in range(cur.rowcount):
            specs.append(cur.fetchone()[0])    
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return specs


def get_all_slots():
    slots = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT start_time, end_time FROM slots;"
        cur.execute(sql)
        
        for i in range(cur.rowcount):
            slots.append(cur.fetchone())     
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return slots


def get_qual_id(qual_name):
    qual_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT qual_id FROM qualification where qual_name=%s;"
        cur.execute(sql, (qual_name,))
        qual_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_id


def get_symptom_id(symptom):
    symp_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT symptom_id FROM symptom where name=%s;"
        cur.execute(sql, (symptom,))
        symp_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return symp_id


def get_symptom_name(id):
    symp = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT name FROM symptom where symptom_id=%s;"
        cur.execute(sql, (id,))
        symp = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return symp


def get_patient_symptoms(patient_id):
    symps = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT symptom_id FROM has_symptom where patient_id=%s;"
        cur.execute(sql, (patient_id,))
        
        for _ in range(cur.rowcount):
            symps.append(cur.fetchone()[0])
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return symps


def get_all_symptoms():
    symptoms = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT name FROM symptom;"
        cur.execute(sql)

        for i in range(cur.rowcount):
            symptoms.append(cur.fetchone()[0])      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return symptoms


def get_history(patient_id):
    conn = None
    hist = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
        SELECT a.appointment_date, a.appointment_time, d.name FROM history h 
        left join appointments a on a.patient_id=h.patient_id 
        left join doctor d on d.doctor_id=a.doctor_id
        where h.patient_id=%s;
        """

        cur.execute(sql, (patient_id, ))

        for i in range(cur.rowcount):
            hist.append(cur.fetchone())
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return hist    


def get_appointments(doctor_id):
    conn = None
    appts = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
        SELECT a.appointment_date, a.appointment_time, p.username, p.age, p.name FROM appointments a 
        left join patient p on p.patient_id=a.patient_id 
        where a.doctor_id=%s;
        """

        cur.execute(sql, (doctor_id, ))

        for i in range(cur.rowcount):
            appts.append(cur.fetchone())
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return appts  


def get_app_id(app_date, app_time, pid, did):
    app_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT appointment_id FROM appointments where appointment_date=%s and appointment_time=%s and patient_id=%s and doctor_id=%s;"
        cur.execute(sql, (app_date, app_time, pid, did))
        app_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return app_id


def get_best_doctor(symptoms_list, pref_time):
    conn = None
    best_doc_id = -1
    pref_time = datetime.strptime(pref_time, '%H:%M').time()
    pref_time = datetime.combine(date.today(), pref_time)

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        priority = dict()
        priority['Chest pain'] = 100
        priority['Breathing trouble'] = 90
        priority['Burns'] = 80
        priority['Fracture'] = 70
        priority['Urinary problems'] = 60
        priority['Diabetes'] = 50
        priority['Skin rashes'] = 40
        priority['Fever'] = 35
        priority['Head ache'] = 30
        priority['Stomach ache'] = 20
        priority['Throat infection'] = 19
        priority['Nose infection'] = 17
        priority['Ear infection'] = 15
        priority['Cold'] = 10
        priority['Tiredness'] = 9

        spec = dict()
        spec['Chest pain'] = 'Cardiology'
        spec['Breathing trouble'] = 'Pulmonology'
        spec['Burns'] = 'Surgury'
        spec['Fracture'] = 'Orthopedia'
        spec['Urinary problems'] = 'Urology'
        spec['Diabetes'] = 'Endocrinology'
        spec['Skin rashes'] = 'Dermetalogy'
        spec['Head ache'] = 'Neurology'
        spec['Stomach ache'] = 'Gastroenterology'
        spec['Throat infection'] = 'ENT'
        spec['Nose infection'] = 'ENT'
        spec['Ear infection'] = 'ENT'
        spec['Cold'] = 'Physician'

        major_problem = 'Cold'

        for s in symptoms_list:
            if priority[s] > priority[major_problem]:
                major_problem = s

        speciality = spec[major_problem]
        # print(speciality)
        spec_id = get_spec_id(speciality)
        # print(spec_id)
        doc_ids = []

        sql = """
        SELECT doctor_id FROM specialized  
        where spec_id=%s;
        """

        cur.execute(sql, (spec_id, ))

        for i in range(cur.rowcount):
            doc_ids.append(cur.fetchone()[0])
               
        print('docids: ', doc_ids)
        
        min_slots = []

        for docid in doc_ids:
            docid = docid[0]

            sql = """
            SELECT s.start_time, s.end_time FROM has_slots hs
            left join slots s on hs.slot_id=s.slot_id 
            where hs.doctor_id=%s;
            """

            cur.execute(sql, (docid, ))

            slots = []
            for i in range(cur.rowcount):
                slot = cur.fetchone()    
                start = datetime.combine(date.today(), slot[0])
                end = datetime.combine(date.today(), slot[1])
                
                # print((end - pref_time).days)
                # print((start - pref_time).days)
                if (start-pref_time).days<0 and (end - pref_time).days>=0:
                    cur.close()
                    conn.close()
                    # print("here")
                    return (docid, slot)

                elif (start-pref_time).days>=0 and (end - pref_time).days>=0:
                    slots.append(slot)

            # print(slots)

            start = datetime.combine(date.today(), slots[0][0])
            end = datetime.combine(date.today(), slots[0][1])

            delta = (start - pref_time).seconds
            best_slot = slots[0]

            for s in slots:
                start = datetime.combine(date.today(), s[0])
                end = datetime.combine(date.today(), s[1])
                
                if (start - pref_time).seconds<delta:
                    best_slot = s
                    delta = (start - pref_time).seconds

            # print(docid)
            min_slots.append((docid,best_slot))

        start = datetime.combine(date.today(), min_slots[0][1][0])
        end = datetime.combine(date.today(), min_slots[0][1][1])
        # pref_time = datetime.combine(date.today(), pref_time)

        delta = (start - pref_time).seconds
        best_slot = min_slots[0][1]
        best_doc_id = min_slots[0][0]
        # print(min_slots)

        for s in min_slots:
            start = datetime.combine(date.today(), s[1][0])
            end = datetime.combine(date.today(), s[1][1])
            
            if (start - pref_time).seconds<delta:
                best_slot = s[1]
                best_doc_id = s[0]
                delta = (start - pref_time).seconds
              

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return (best_doc_id, best_slot)
