import pickle
with open('1.txt', 'rb') as f:
    new=pickle.load(f)
with open('2.txt', 'rb') as f:
    similarity=pickle.load(f)
z=True
def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    print()
    print(movie)
    for i in distances[1:13]:
        if new.iloc[i[0]].title == movie:
            continue
        else:
            print(new.iloc[i[0]].title) 
            
    return z
x=True
while(x==True): 
        try:
            mess=input("enter movie name : ")
            mess=mess.title()
            recommend(mess)
        except:
            import imdb
            ia = imdb.IMDb()
            search = ia.search_movie(mess)  
            for i in range(len(search)):    
               id = search[i].movieID    
            
            for i in range(len(search)):
             try:
               recommend(search[i]['title'])
               if z==True:
                   break
             except:
                if i==len(search)-1:
                    print("\nThere is no search found")
                continue
              
        print("\nDo you want to search another movie : ",end="")
        n=input()
        if n=="yes" or n=="y" or n=="Y" or n=="Yes":
            continue
        else:
            x=False