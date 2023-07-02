from telegram import ForceReply, Update
from telegram.ext import ContextTypes
from main import recsys

async def getrecommend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   teks = update.message.text.replace("/recommend_me_film_by_synopsis ", "")
   result = recsys.recommend(teks)
   res = ""
   for id, ind in enumerate(result.index):
      res += f"""
{id+1}. {result['title'][ind]} - {result['runtime'][ind]} Menit"""
   res += """
Note:
- Rekomendasi hanya berdasarkan kemiripan sinopsis film yang diberikan, tidak dipengaruhi hal lainnya seperti genre, maupun rating
- Rekomendasi pertama adalah film sesuai sinopsis yang diberikan atau yang mendekati
- Rekomendasi tidak tepat? silakan ambil sinopsis film yang dimaksud dari website https://www.themoviedb.org

- data film cuma sampe awal 2019. wkwkwk
   """
   await update.message.reply_text(res)