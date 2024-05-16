@bot.command()
async def mem(ctx):
    randmeme = random.randint(1,3)
    if randmeme == 1:
        with open('Memes/mem1.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
            picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)
    elif randmeme == 2:
        with open('Memes/mem2.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
            picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)
    elif randmeme == 3:
        with open('Memes/mem3.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
            picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    rate = random.randint(1, 10)
    with open('Memes/mem1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    rate = random.randint(1, 10)
    with open('Memes/mem2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    rate = random.randint(1, 10)
    with open('Memes/mem3.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    with open('Memes/animal.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
