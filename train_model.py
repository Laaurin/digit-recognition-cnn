from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


num = train_images[1]
for i in range(len(num)):
    line = ""
    for j in range(len(num[i])):
        line += f"{num[i][j]:3} "
    print(line)
print(num.shape)

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255.0
train_labels = to_categorical(train_labels)

test_images = test_images.astype('float32') / 255.0
test_labels = to_categorical(test_labels)



model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

#model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#model.fit(train_images, train_labels, validation_data=(test_images, test_labels), epochs=4, batch_size=128)

#model.save('my_model.h5')
