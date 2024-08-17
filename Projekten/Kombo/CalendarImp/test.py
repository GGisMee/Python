def group_lesson_details(data):
    grouped_lessons = []
    i = 0
    times = []
    
    # First, extract all time entries
    for item in data:
        if len(item) == 1 and item[0].count(':') == 1:
            times.append(item[0])
    
    while i < len(data):
        # Check if we're at the start of a lesson entry
        if len(data[i]) == 1 and not data[i][0].startswith(tuple(times)):
            subject = data[i][0]
            
            # Skip entries like 'Lunch Åk3'
            if subject.lower().startswith('lunch') or subject.lower() == 'studieverkstad':
                i += 1
                continue
            
            # Find the next valid teacher entry
            j = i + 1
            while j < len(data) and (len(data[j]) == 1 or data[j][0].isdigit()):
                j += 1
            teachers = data[j] if j < len(data) else []
            
            # Find the next valid room entry
            k = j + 1
            while k < len(data) and (len(data[k]) != 1 or not data[k][0].isdigit()):
                k += 1
            room = data[k][0] if k < len(data) else ''
            
            # Find start and end times
            start_time = find_nearest_time(times, i)
            end_time = find_next_time(times, start_time)
            
            grouped_lessons.append([subject, teachers, room, start_time, end_time])
            i = k + 1
        else:
            i += 1
    
    return grouped_lessons

def find_nearest_time(times, index):
    for time in reversed(times[:index+1]):
        if time in [item[0] for item in raw_data[:index+1]]:
            return time
    return ''

def find_next_time(times, start_time):
    start_index = times.index(start_time)
    if start_index + 1 < len(times):
        return times[start_index + 1]
    return ''

# Convert the string representation of the list to an actual list
import ast
raw_data = ast.literal_eval("[['Aktivitet UPPSTARSDAG'], ['ANNHAL', 'STEMOB'], ['21'], ['ENGENG07'], ['STEMOB'], ['21'], ['Lunch Åk3'], ['PRDPRO01'], ['MARSAM'], ['21'], ['MATMAT04'], ['ANNHAL'], ['21'], ['PROFILHS'], ['JONWES', 'JOHOST', 'MARSTR'], ['21'], ['PROFILNV'], ['JOSBRO'], ['Labb'], ['PROFILTD'], ['PARHEN', 'ANDJIL'], ['42'], ['HISHIS01a1'], ['JONWES'], ['21'], ['PRDPRO01'], ['MARSAM'], ['21'], ['Lunch Åk3'], ['PRUPRD01S'], ['SVEKRI'], ['22'], ['PROFILHS'], ['JONWES', 'JOHOST', 'MARSTR'], ['21'], ['PROFILNV'], ['HELDAM'], ['Labb'], ['PROFILTD'], ['PARHEN', 'ANDJIL'], ['42'], ['PROFILHS'], ['JONWES', 'JOHOST', 'MARSTR'], ['21'], ['PROFILNV'], ['HELDAM'], ['41'], ['PROFILTD'], ['PARHEN', 'ANDJIL'], ['42'], ['Lunch Åk3'], ['SVESVE03'], ['MARSTR'], ['21'], ['Studieverkstad'], ['42', '41'], ['SVESVE03'], ['MARSTR'], ['21'], ['SVASVA03'], ['JUDBEC'], ['22'], ['MATMAT04'], ['ANNHAL'], ['21'], ['Lunch Åk3'], ['ENGENG07'], ['STEMOB'], ['21'], ['HISHIS01a1'], ['JONWES'], ['21'], ['PROFILHS'], ['JONWES', 'JOHOST', 'MARSTR'], ['21'], ['PROFILNV'], ['JOSBRO'], ['Labb'], ['PROFILTD'], ['PARHEN', 'ANDJIL'], ['42'], ['PROFILHS'], ['JONWES', 'JOHOST', 'MARSTR'], ['21'], ['PROFILNV'], ['JOSBRO'], ['Labb'], ['PROFILTD'], ['PARHEN', 'ANDJIL'], ['42'], ['Lunch Åk3'], ['Utvärderingstid'], ['ANNHAL', 'STEMOB'], ['21'], ['PRUPRD01S'], ['SVEKRI'], ['22'], ['Studieverkstad'], ['42'], ['8:10'], ['9:30'], ['9:50'], ['10:55'], ['10:55'], ['12:10'], ['12:10'], ['14:15'], ['14:35'], ['16:10'], ['14:35'], ['16:10'], ['8:10'], ['9:30'], ['9:50'], ['10:55'], ['10:55'], ['12:10'], ['12:10'], ['14:15'], ['8:10'], ['9:30'], ['9:50'], ['10:55'], ['10:55'], ['12:10'], ['12:10'], ['14:15'], ['14:35'], ['16:10'], ['8:10'], ['9:30'], ['9:50'], ['10:55'], ['10:55'], ['12:10'], ['12:10'], ['14:15'], ['14:35'], ['16:10'], ['8:10'], ['9:30'], ['9:50'], ['10:55'], ['10:55'], ['12:10'], ['12:10'], ['12:55'], ['13:00'], ['15:00'], ['15:15'], ['17:00']]")

# Apply the grouping function
grouped_lessons = group_lesson_details(raw_data)

# Print the result
for lesson in grouped_lessons:
    print(f"Subject: {lesson[0]}")
    print(f"Teachers: {', '.join(lesson[1])}")
    print(f"Room: {lesson[2]}")
    print(f"Start time: {lesson[3]}")
    print(f"End time: {lesson[4]}")
    print("--------------------")