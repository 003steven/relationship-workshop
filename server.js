const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3002;

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`💞 亲密关系深度共建研习会官网运行在 http://localhost:${PORT}`);
  console.log('✨ 高端课程展示页面已加载完成');
});
