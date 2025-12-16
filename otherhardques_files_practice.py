# # with open("secretmessage.txt", encoding="utf-8") as f:
# #     line_buffer = ""

# #     for ch in f.read():
# #         if ch == '\n':
# #             if line_buffer:
# #                 print(line_buffer)
# #                 line_buffer = ""
# #             continue

# #         if ord(ch) < 32 or ord(ch) > 126:
# #             line_buffer += ch

# #     if line_buffer:
# #         print(line_buffer)

# # # # 2]Implement the class of Stacks and Queues:
# # # 3] Implementing the scores average of the team:
# team = []
# team_dict_avg={}
# count =0
# with open("scores.txt") as f:
#     s= f.readlines()
#     for mainline in s:
#         line = mainline.split()
#         team.append([line[0],line[1], int(line[2]),line[3], int(line[4])])
#     # print(team)
# for indteam in team:
#     count+=1
#     team_dict_avg[indteam[1]] = team_dict_avg.get(indteam[1],0)+indteam[2]
#     team_dict_avg[indteam[3]] = team_dict_avg.get(indteam[3],0)+indteam[4]
# for teamname, score in team_dict_avg.items():
#     team_dict_avg[teamname] = score/count
# print(team_dict_avg)

# print("Total avg score based on the game: ")
# totalscore=0
# c=0
# for i in team:
#     c+=1
#     indscore = i[2]+i[4]
#     totalscore += indscore
#     print("Total score of the team",c," : ",indscore/len(team))
#     indscore = 0
# print("Total score",totalscore)
# print(" Average",totalscore/len(team))
# # Pick your favorite team and scan through the file to determine how 
# # many games they won and how many games they lost.
# n = input("Eneter the name of the team you want to search: ")
# w_c = 0
# l_c=0
# for x in team:
#     if n in x:
#         if x[1] == n:
#             if x[2]>x[4]:
#                 w_c +=1
#             else:
#                 l_c +=1
#         if x[3] == n:
#             if x[4] >x[2]:
#                 w_c+=1
#             else:
#                 l_c+=1
# print(w_c ," -- win")
# print(l_c, " -- l_c")
# print(team)
# # Find the team(s) that lost by 30 or more points the most times
# lostd={}
# lost= []
# for i in team:
#     if i[2]-i[4]>30:
#         lost.append(i[3])
#     if i[2]-i[4]<30:
#         lost.append(i[1])
# # print(lost)
# for y in lost:
#     lostd[y] = lostd.get(y,0)+1
# print(lostd)
# lostd = sorted(lostd.items(), key=lambda x :x[1], reverse = True)[0]
# print(lostd)

# # finding the team tat averaged atleast 70 points in a game!
# avd={}
# for x in team:
#     team1= x[1]
#     team2= x[3]
#     avd[team1] = avd.get(team1,[])+[x[2]]
#     avd[team2] = avd.get(team1,[])+[x[4]]
# print(avd)

# print("Team names who scored above 70 avg is: ")
# for n , sl in avd.items():
#     if sum(sl)/len(sl) >= 70:
#         print("Team name: ", n , " avg score: ", sum(sl)/len(sl))

# # #(e) Find all the teams that had winning records but 
# # were collectively outscored by their opponents.
# # A team is collectively outscored by their opponents if the 
# # total number of points the team scored over all their games is less 
# # than the totalnumber of points their opponents scored in their games against the team

# d={}
# for i in team:
#     if i[1] not in d:
#         d[i[1]] = {'win':0, 'loss':0, 'myscore':0,'oppscore':0}
#     if i[3] not in d:
#         d[i[3]] = {'win':0, 'loss':0, 'myscore':0,'oppscore':0}
#     if i[2]>i[4]:
#         d[i[1]]['win']+=1
#         d[i[3]]['loss']+=1
#     else:
#         d[i[3]]['win']+=1
#         d[i[1]]['loss']+=1
# for date, t1, s1, t2, s2 in team:
#     d[t1]['myscore']+=s1
#     d[t1]['oppscore']+=s2
#     d[t2]['myscore']+=s2
#     d[t2]['oppscore']+=s1
# for i,j in d.items():
#     if j['win']>j['loss'] and j['myscore']<j['oppscore']:
#         print(i)

# You are given a file namelist.txt that contains a bunch of names.Some of the names 
# are a first name and a last name separated byspaces, like George Washington, while others have a middle name,like John Quincy Adams. There are no names consisting of just oneword or more than three words. Write a program that asks the user toenter initials, like GW or JQA, and prints all the names that matchthose 
# initials. Note that initials like JA should match both John Adamsand John Quincy Adams