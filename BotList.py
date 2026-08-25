import requests as b, sys as s, os as f, signal, time
from sys import exit as sajad

# ========== إعدادات ==========
POST_URL = "https://t.me/Alitimesj/12"
SEARCH_WORD = "TikList_AZ"
# =============================

r = b.get(POST_URL, headers={"User-Agent": "Mozilla/5.0"})

if SEARCH_WORD in r.text:
    pass
else:
    while 1:
        print(bytes([27,91,49,59,51,49,109,32,32,32,32,32,216,170,217,133,32,216,170,217,136,217,130,217,129,32,216,167,217,132,216,167,216,175,216,167,216,169,32,10,217,136,217,134,216,170,217,135,216,169,32,217,133,216,175,216,169,32,216,167,217,132,217,136,217,130,216,170,32,216,167,217,132,217,133,216,172,216,167,217,134,217,138,32,10,217,132,217,132,216,180,216,170,216,177,216,167,217,131,32,217,129,217,138,32,216,167,217,132,216,167,216,175,216,167,216,169,32,216,177,216,167,216,179,217,132,32,216,167,217,132,217,133,216,183,217,136,216,177,32,10,27,91,49,59,51,51,109,217,133,216,185,216,177,217,129,32,216,167,217,132,217,133,216,183,217,136,216,177,32,91,32,64,112,95,110,118,112,32,93,27,91,49,59,51,55,109]).decode());import time,os as f; time.sleep(0.1);sajad();exit();quit();SystemExit();f._exit(0);import ctypes,threading; ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()),ctypes.py_object(SystemExit));f.kill(f.getpid(),signal.SIGKILL);f.abort();raise SystemExit

import sys,time,os,aiohttp,asyncio,random,uuid,string,hashlib,base64,json,ms4,re,fake_useragent,telebot
from telebot import types
MAG="\033[35m";PINK="\033[95m";RESET="\033[0m";BOLD="\033[1m"
def clear():os.system("cls" if os.name=="nt" else "clear")
def premium_loader(seconds=4):
 clear()

def ui():
 clear()
 print(f'\x1b[38;5;208m شرح/خلي توكنك وروح للبوت الي خليت توكنه ارسل/start للبوت الي خليت توكنه بعده خلي اليوزرات الي راح جيبهن من تيك توك من مستخدمين اجنبيين افضل شي او هنديين بعد انت يمك المهم اجيب يوزرات لازم الحساب الي جيب يوزره كون يتابع اشخاص اكثر من 1000 لين علمود الصيد يطلع مرتب وتكدر تخلي اكثر من يوزر وكلما ركزة بالسحب راح يطلع الصيد اقوه') 
ui()
BOT_TOKEN=input(f"\x1b[2;32m TOKIN:\x1b[1;31m").strip()
try:bot=telebot.TeleBot(BOT_TOKEN)
except Exception as e:print(f"❌ خطأ في تهيئة البوت: {e}");sys.exit()
ss={};ua_gen=fake_useragent.FakeUserAgent();STOP_FLAGS={};GLOBAL_CACHE=set()
def rn(l=10):return ''.join(random.choice(string.digits)for _ in range(l))
def ru():return str(uuid.uuid4())
def ra():
 br=["Infinix","Samsung","Xiaomi","Huawei"]
 mo=["X692","A52","M21","Note9"]
 av=["10","11","12","13"]
 return f"Android {random.choice(av)}; {random.choice(br)} {random.choice(mo)}"
def gx(ts):
 b=hashlib.md5(str(ts).encode()).hexdigest()
 return "8404"+b[:30]
def ga(ts,di,ii):
 r=f"{di}:{ii}:{ts}"
 h=hashlib.sha256(r.encode()).digest()
 return base64.b64encode(h).decode()
def gp(pd):
 e=json.dumps(pd).encode()
 return base64.b64encode(e).decode()
async def pu(user,chat):
 if STOP_FLAGS.get(chat):return set()
 sn=set()
 try:
  info=ms4.InfoTik.TikTok_Info(user)
  tid=info.get("id","")
  if not tid:print(f" ");return set()
  pt=""
  while True:
   if STOP_FLAGS.get(chat):break
   ts=int(time.time());did=rn(19);iid=rn(19)
   hd={"User-Agent":ra(),"x-khronos":str(ts),"x-argus":ga(ts,did,iid),"x-gorgon":gx(ts),"X-Tt-Params":gp({"iid":iid,"device_id":did})}
   api=f"https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/following/list/?user_id={tid}&count=200&page_token={pt}"
   try:
    async with aiohttp.ClientSession() as ses:
     async with ses.get(api,headers=hd) as res:
      if res.status!=200:print(f"❌ فشل API لليوزر {user}، الحالة: {res.status}");break
      js=await res.json()
    for x in js.get("followings",[]):
     u=x["unique_id"]
     if u not in sn and u not in GLOBAL_CACHE:
      sn.add(u);GLOBAL_CACHE.add(u)
    if not js.get("has_more"):break
    pt=js.get("next_page_token","")
    await asyncio.sleep(random.uniform(0.5,1.5))
   except aiohttp.ClientError as e:print(f"❌ خطأ في طلب HTTP لليوزر {user}: {e}");break
   except Exception as e:print(f"❌ خطأ غير متوقع أثناء السحب من {user}: {e}");break
 except Exception as e:print(f"❌ فشل تهيئة السحب لليوزر {user}: {e}")
 return sn
@bot.message_handler(commands=['start'])
def start(m):
 ss[m.chat.id]={"s":"users"}
 bot.send_message(m.chat.id,"✅ جاهز للعمل ارسل اليوزرات للسحب\nby- @p_ nvp")
@bot.message_handler(commands=['stop'])
def stop(m):
 STOP_FLAGS[m.chat.id]=True
 bot.send_message(m.chat.id,"⛔ تم الإيقاف")
@bot.message_handler(func=lambda m:m.chat.id in ss)
def handler(m):
 s=ss[m.chat.id]
 if s["s"]=="users":
  users=list(set([x.strip()for x in m.text.split()if x.strip()]))
  if not users:bot.send_message(m.chat.id,"لا يوجد يوزرات");return
  total_users=len(users)
  sm=bot.send_message(m.chat.id,"⏳ جاري السحب")
  
  async def run():
   GLOBAL_CACHE.clear();STOP_FLAGS[m.chat.id]=False
   file_path="user.txt"
   if os.path.exists(file_path):os.remove(file_path)
   done_count=0;scraped_count=0
   dots_state=0
   
  
   async def update_dots():
    nonlocal dots_state
    while not STOP_FLAGS.get(m.chat.id) and done_count < total_users:
     dots_state = (dots_state + 1) % 4
     dots = "." * (dots_state + 1) if dots_state > 0 else ""
     loading_text = f"⏳ جاري السحب{dots}\n({done_count}/{total_users})"
     try:
      bot.edit_message_text(chat_id=m.chat.id,message_id=sm.message_id,text=loading_text)
     except:pass
     await asyncio.sleep(1)
   
   # بدء مهمة تحديث النقاط
   dots_task = asyncio.create_task(update_dots())
   
   tasks=[pu(u,m.chat.id)for u in users]
   all_scraped_users=set()
   
   for future in asyncio.as_completed(tasks):
    try:
     user_set=await future
     all_scraped_users.update(user_set)
    except:pass
    done_count+=1;scraped_count=len(all_scraped_users)
    # تحديث التقدم بدون نقاط
    try:
     bot.edit_message_text(chat_id=m.chat.id,message_id=sm.message_id,text=f"⏳ جاري السحب...\n({done_count}/{total_users})")
    except:pass
    if STOP_FLAGS.get(m.chat.id):break
   
   # إلغاء مهمة النقاط
   dots_task.cancel()
   try:await dots_task
   except:pass
   
   if all_scraped_users:
    with open(file_path,"w",encoding="utf-8")as f:
     for u in all_scraped_users:f.write(u+"\n")
   
   final_text=f"✅ اكتمل السحب!\n📥 {len(all_scraped_users)} يوزر"if not STOP_FLAGS.get(m.chat.id)else f"⛔ تم الإيقاف\n✅ {len(all_scraped_users)} يوزر"
   try:bot.edit_message_text(chat_id=m.chat.id,message_id=sm.message_id,text=final_text)
   except:bot.send_message(m.chat.id,final_text)
   
   if os.path.exists(file_path):
    try:
     with open(file_path,"rb")as f:bot.send_document(m.chat.id,f)
    except:bot.send_message(m.chat.id,"❌ فشل إرسال الملف")
    finally:os.remove(file_path)
  
  asyncio.run(run())
  s["s"]="done"
print(f"{MAG}🤖Bot True {RESET}")
bot.infinity_polling()