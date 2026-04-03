# GitHub配置指南

## 项目GitHub仓库配置

### 步骤1：创建GitHub仓库
1. 登录GitHub (https://github.com)
2. 点击右上角"+"按钮，选择"New repository"
3. 仓库名称：枕边降噪设备
4. 描述：枕边主动降噪设备项目仓库
5. 选择Public（公开）或Private（私有）
6. 点击Create repository

### 步骤2：配置远程仓库
仓库创建成功后，你会看到Git URL：
- HTTPS URL: https://github.com/<你的用户名>/枕边降噪设备.git

将此URL添加到本地仓库：

```bash
cd /root/.openclaw/workspace/projects/降噪设备
git remote add origin https://github.com/<你的用户名>/枕边降噪设备.git
```

### 步骤3：推送代码
第一次推送：

```bash
git push -u origin master
```

### 步骤4：配置SSH密钥（可选）
如果需要SSH访问，创建SSH密钥：

```bash
ssh-keygen -t ed25519 -C "枕边降噪设备项目"
```

然后将公钥添加到GitHub：
1. 在GitHub Settings > SSH and GPG keys
2. 点击New SSH key
3. 粘贴公钥内容

### 备选方案：使用GitHub CLI
如果你有GitHub CLI，可以使用：

```bash
gh auth login
gh repo create 枕边降噪设备 --public --source=. --push
```

### 备选方案：使用GitHub token
如果你有GitHub token，可以设置环境变量：

```bash
export GITHUB_TOKEN=你的token
git push origin master
```

## 本地Git仓库状态

当前本地仓库包含：
- README.md - 项目说明
- 文档/ - 项目规划和配置文档
- 嵌入式/ - STM32配置文件
- 算法/ - 即将开发的算法代码
- 硬件/ - PCB设计文档
- 声学/ - 声学设计文档
- 测试/ - 测试验证文档

## GitHub仓库结构建议

建议在GitHub仓库中创建以下结构：
```
/
├── README.md
├── docs/
│   ├── 枕边降噪设备项目配置.md
│   ├── agent配置示例.yaml
│   ├── profiles.yaml
│   ├── 项目启动指南.md
│   ├── GitHub配置指南.md
│   └── stm32_config.md
├── firmware/
├── algorithms/
├── hardware/
├── acoustics/
└── tests/
```

## 配置GitHub Webhooks
配置Webhooks以便自动部署：
1. 仓库Settings > Webhooks
2. 添加Webhook推送事件
3. 设置触发动作（如CI/CD）

## 项目协作流程
1. 每日提交到GitHub主分支
2. 使用GitHub Issues记录问题和需求
3. 使用GitHub Projects管理任务
4. 使用GitHub Actions进行自动化测试

## 注意事项
1. 确保代码质量：使用embedded-review技能审查代码
2. 保持文档更新：README.md定期更新
3. 保护敏感信息：不要推送配置文件中的私密信息