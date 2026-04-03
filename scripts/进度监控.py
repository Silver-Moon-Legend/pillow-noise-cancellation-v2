#!/usr/bin/env python3
"""
枕边降噪设备项目进度监控脚本
项目经理用于监控各专家进度
"""

import os
import json
import datetime

class ProjectMonitor:
    def __init__(self):
        self.project_dir = "/root/.openclaw/workspace/projects/降噪设备"
        self.tasks_file = f"{self.project_dir}/文档/任务跟踪.md"
        
    def read_tasks(self):
        """读取任务跟踪文件"""
        tasks = {}
        current_section = ""
        
        with open(self.tasks_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for line in lines:
            # 检测任务类别
            if line.startswith("### 算法专家任务"):
                current_section = "algorithm"
            elif line.startswith("### 嵌入式专家任务"):
                current_section = "embedded"
            elif line.startswith("### 硬件专家任务"):
                current_section = "hardware"
            elif line.startswith("### 声学专家任务"):
                current_section = "acoustic"
            elif line.startswith("### 测试工程师任务"):
                current_section = "test"
            elif line.startswith("### 项目经理任务"):
                current_section = "manager"
            
            # 解析任务行
            if line.startswith("|"):
                parts = line.split("|")
                if len(parts) >= 7:
                    task_id = parts[1].strip()
                    description = parts[2].strip()
                    status = parts[3].strip()
                    responsible = parts[4].strip()
                    start_date = parts[5].strip()
                    end_date = parts[6].strip()
                    completion = parts[7].strip()
                    
                    if task_id and task_id != "任务ID":
                        task_key = f"{current_section}_{task_id}"
                        tasks[task_key] = {
                            "task_id": task_id,
                            "description": description,
                            "status": status,
                            "responsible": responsible,
                            "start_date": start_date,
                            "end_date": end_date,
                            "completion": completion,
                            "section": current_section
                        }
        
        return tasks
    
    def check_task_progress(self):
        """检查任务进度"""
        tasks = self.read_tasks()
        
        # 检查算法专家进度
        algorithm_tasks = [t for t in tasks.values() if t["section"] == "algorithm"]
        algorithm_in_progress = [t for t in algorithm_tasks if t["status"] == "进行中"]
        algorithm_completed = [t for t in algorithm_tasks if t["status"] == "已完成"]
        algorithm_not_started = [t for t in algorithm_tasks if t["status"] == "待开始"]
        
        # 检查嵌入式专家进度
        embedded_tasks = [t for t in tasks.values() if t["section"] == "embedded"]
        embedded_in_progress = [t for t in embedded_tasks if t["status"] == "进行中"]
        embedded_completed = [t for t in embedded_tasks if t["status"] == "已完成"]
        embedded_not_started = [t for t in embedded_tasks if t["status"] == "待开始"]
        
        return {
            "algorithm": {
                "total": len(algorithm_tasks),
                "in_progress": len(algorithm_in_progress),
                "completed": len(algorithm_completed),
                "not_started": len(algorithm_not_started),
                "in_progress_details": algorithm_in_progress
            },
            "embedded": {
                "total": len(embedded_tasks),
                "in_progress": len(embedded_in_progress),
                "completed": len(embedded_completed),
                "not_started": len(embedded_not_started),
                "in_progress_details": embedded_in_progress
            },
            "hardware": {
                "total": len([t for t in tasks.values() if t["section"] == "hardware"]),
                "in_progress": len([t for t in tasks.values() if t["section"] == "hardware" and t["status"] == "进行中"]),
                "completed": len([t for t in tasks.values() if t["section"] == "hardware" and t["status"] == "已完成"]),
                "not_started": len([t for t in tasks.values() if t["section"] == "hardware" and t["status"] == "待开始"]),
            },
            "acoustic": {
                "total": len([t for t in tasks.values() if t["section"] == "acoustic"]),
                "in_progress": len([t for t in tasks.values() if t["section"] == "acoustic" and t["status"] == "进行中"]),
                "completed": len([t for t in tasks.values() if t["section"] == "acoustic" and t["status"] == "已完成"]),
                "not_started": len([t for t in tasks.values() if t["section"] == "acoustic" and t["status"] == "待开始"]),
            },
            "test": {
                "total": len([t for t in tasks.values() if t["section"] == "test"]),
                "in_progress": len([t for t in tasks.values() if t["section"] == "test" and t["status"] == "进行中"]),
                "completed": len([t for t in tasks.values() if t["section"] == "test" and t["status"] == "已完成"]),
                "not_started": len([t for t in tasks.values() if t["section"] == "test" and t["status"] == "待开始"]),
            },
            "manager": {
                "total": len([t for t in tasks.values() if t["section"] == "manager"]),
                "in_progress": len([t for t in tasks.values() if t["section"] == "manager" and t["status"] == "进行中"]),
                "completed": len([t for t in tasks.values() if t["section"] == "manager" and t["status"] == "已完成"]),
                "not_started": len([t for t in tasks.values() if t["section"] == "manager" and t["status"] == "待开始"]),
            }
        }
    
    def check_actual_files(self):
        """检查实际文件进度"""
        actual_progress = {}
        
        # 检查算法专家文件
        algorithm_dir = f"{self.project_dir}/算法"
        if os.path.exists(algorithm_dir):
            algorithm_files = os.listdir(algorithm_dir)
            algorithm_progress_files = len([f for f in algorithm_files if f.startswith("A")])
            actual_progress["algorithm"] = algorithm_progress_files
        
        # 检查嵌入式专家文件
        embedded_dir = f"{self.project_dir}/嵌入式"
        if os.path.exists(embedded_dir):
            embedded_files = os.listdir(embedded_dir)
            embedded_progress_files = len([f for f in embedded_files if f.startswith("E")])
            actual_progress["embedded"] = embedded_progress_files
        
        return actual_progress
    
    def generate_report(self):
        """生成进度报告"""
        task_progress = self.check_task_progress()
        actual_files = self.check_actual_files()
        
        report_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        report = f"""
# 枕边降噪设备项目进度报告
报告时间：{report_date}

## 总体进度
- **算法专家**：{task_progress['algorithm']['in_progress']}/{task_progress['algorithm']['total']} 任务进行中
- **嵌入式专家**：{task_progress['embedded']['in_progress']}/{task_progress['embedded']['total']} 任务进行中
- **硬件专家**：{task_progress['hardware']['in_progress']}/{task_progress['hardware']['total']} 任务进行中
- **声学专家**：{task_progress['acoustic']['in_progress']}/{task_progress['acoustic']['total']} 任务进行中
- **测试工程师**：{task_progress['test']['in_progress']}/{task_progress['test']['total']} 任务进行中
- **项目经理**：{task_progress['manager']['in_progress']}/{task_progress['manager']['total']} 任务进行中

## 文件进度检查
- **算法专家文件**：{actual_files.get('algorithm', 0)} 个进度文件
- **嵌入式专家文件**：{actual_files.get('embedded', 0)} 个进度文件

## 具体进度详情
### 算法专家（任务A1：进行中，40%）
- PDM麦克风阵列信号处理研究
- 进度文件：{actual_files.get('algorithm', 0)} 个文件

### 嵌入式专家（任务E1：进行中，30%）
- STM32L496VGT6引脚配置
- 进度文件：{actual_files.get('embedded', 0)} 个文件

## 需要关注的问题
1. 硬件专家和声学专家尚未开始工作
2. 需要尽快启动其他专家的工作

## 建议行动
1. 督促硬件专家开始STM32外围电路设计
2. 督促声学专家开始喇叭腔体声学优化
3. 继续监控算法和嵌入式专家进度
        """
        
        return report
    
    def save_report(self):
        """保存进度报告"""
        report = self.generate_report()
        report_date = datetime.datetime.now().strftime("%Y-%m-%d")
        report_file = f"{self.project_dir}/文档/进度监控报告_{report_date}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"进度报告保存到：{report_file}")
        return report_file

if __name__ == "__main__":
    monitor = ProjectMonitor()
    report = monitor.generate_report()
    report_file = monitor.save_report()
    
    # 打印报告摘要
    print(report)