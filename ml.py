def machine(): 
        sum=0
        i=0    
        import tensorflow as tf
        from tensorflow import keras
        model=keras.models.load_model("model.h5")
        word_index =  keras.datasets.imdb.get_word_index()
        word_index={k:(v+3) for k,v in word_index.items()}
        word_index["<PAD>"]=0
        word_index["<START>"]=1
        word_index["<UNK>"]=2
        word_index["<UNUSED>"]=3

        def review_encode(s):
                encoded = [1]

                for word in s:
                        if word.lower() in word_index:
                                encoded.append(word_index[word.lower()])
                        else:
                                encoded.append(2)

                return encoded

        with open("test.txt", encoding="utf-8") as f:
                for line in f.readlines():
                        if(line=='\n'):
                                continue
                        nline = line.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace(":", "").replace("\"","").strip().split(" ")
                        encode = review_encode(nline)
                        encode = keras.preprocessing.sequence.pad_sequences([encode], value=word_index["<PAD>"], padding="post", maxlen=250)
                        predict = model.predict(encode)
                        print(line)
                        print(encode)
                        print(predict[0])
                        i=i+1
                        sum=sum+predict[0]
                print(i)
                if(i==0):
                        return [-1]
                return (sum/i)