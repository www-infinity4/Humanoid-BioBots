import app from './api/server';

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Humanoid-BioBots safe validator running on :${port}`);
});
