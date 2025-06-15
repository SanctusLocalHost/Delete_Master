import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from datetime import datetime
from tkcalendar import DateEntry # Mantido para seleção de data

try:
    from PIL import Image, ImageTk # Mantido para compatibilidade futura
except ImportError:
    messagebox.showerror("Erro de Importação", "A biblioteca Pillow é necessária. Instale-a usando 'pip install Pillow'.")

class WarningPopup(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master_app = master
        self.lift()
        self.attributes("-topmost", True)
        self.title("Aviso Importante!")
        self.geometry("550x200")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._on_close_popup)

        popup_bg_color = "#101010"
        text_color_warning = "#FFD700"
        button_color_confirm = "#00FFFF"
        button_hover_color = "#FF00FF"

        self.configure(fg_color=popup_bg_color)

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        warning_text = (
            "ATENÇÃO!!!\n\n"
            "Este programa realiza a Exclusão de Arquivos. Utilize-o apenas se tiver Pleno Conhecimento "
            "das suas ações, e dos Diretórios Selecionados.\n"
            "- O uso indevido pode resultar na PERDA IRREVERSÍVEL DE DADOS, incluindo Arquivos do Sistema."
        )
        
        label = ctk.CTkLabel(main_frame, text=warning_text, text_color=text_color_warning,
                               font=ctk.CTkFont(size=13, weight="bold"), wraplength=500, justify="center")
        label.pack(pady=(10, 20))

        confirm_button = ctk.CTkButton(main_frame, text="ESTOU CIENTE E QUERO PROSSEGUIR",
                                       command=self._confirm_and_proceed,
                                       fg_color=button_color_confirm,
                                       hover_color=button_hover_color,
                                       text_color="#000000",
                                       font=ctk.CTkFont(size=12, weight="bold"))
        confirm_button.pack(pady=10, ipady=5)
        
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def _confirm_and_proceed(self):
        self.destroy()
        self.master_app.show_main_window()

    def _on_close_popup(self):
        self.master_app.quit()
        self.master_app.destroy()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Delete Master V1.4 - Cyberpunk Edition")
        self.geometry("750x780") 

        self.amoled_black = "#000000"
        self.cyber_fg_color = "#0D0D0D" 
        self.text_color = "#AFEEEE" 
        self.entry_text_color = "#E0E0E0"
        self.button_color = "#00FFFF" 
        self.button_hover_color = "#FF00FF"
        self.checkbox_color = "#39FF14"
        self.label_header_color = "#00BFFF"
        self.progress_bar_color = "#FF00FF" 
        self.progress_text_color = "#FFFFFF" 

        self.configure(fg_color=self.amoled_black)

        self.withdraw() 
        self.warning_popup = WarningPopup(self)

        self.var_xlsx = ctk.BooleanVar()
        self.var_docx = ctk.BooleanVar()
        self.var_pdf = ctk.BooleanVar()
        self.var_xml = ctk.BooleanVar()
        self.var_zip = ctk.BooleanVar()
        self.var_ogg = ctk.BooleanVar()
        self.var_png = ctk.BooleanVar()
        self.var_jpeg = ctk.BooleanVar()
        self.var_py = ctk.BooleanVar()
        self.var_exe = ctk.BooleanVar()
        self.var_pyw = ctk.BooleanVar()

    def show_main_window(self):
        self._setup_ui()
        self.deiconify()
        self.attributes("-topmost", False)
        self.lift()
        self.focus_force()

    def _setup_ui(self):
        content_frame = ctk.CTkFrame(self, fg_color="transparent")
        content_frame.pack(padx=20, pady=(20,0), expand=True, fill="both")
        
        dir_frame_outer = ctk.CTkFrame(content_frame, fg_color=self.cyber_fg_color, corner_radius=10)
        dir_frame_outer.pack(pady=10, padx=10, fill="x")
        dir_frame_inner = ctk.CTkFrame(dir_frame_outer, fg_color="transparent")
        dir_frame_inner.pack(pady=5, padx=10, fill="x")

        ctk.CTkLabel(dir_frame_inner, text="Selecione o Diretório:", text_color=self.label_header_color, font=ctk.CTkFont(size=14, weight="bold")).pack(side="left", padx=(0,10))
        self.entrada_diretorio = ctk.CTkEntry(dir_frame_inner, width=350, text_color=self.entry_text_color, fg_color="#1A1A1A", border_color=self.button_color)
        self.entrada_diretorio.pack(side="left", expand=True, fill="x", padx=(0,10))
        ctk.CTkButton(dir_frame_inner, text="Procurar", command=self.selecionar_diretorio, 
                      fg_color=self.button_color, hover_color=self.button_hover_color, text_color="#000000").pack(side="left")

        date_frame_outer = ctk.CTkFrame(content_frame, fg_color=self.cyber_fg_color, corner_radius=10)
        date_frame_outer.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(date_frame_outer, text="Intervalo de Tempo:", text_color=self.label_header_color, font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(5,5), padx=10)
        
        date_frame_inner = ctk.CTkFrame(date_frame_outer, fg_color="transparent")
        date_frame_inner.pack(pady=5, padx=10, fill="x")

        frame_data_inicial = ctk.CTkFrame(date_frame_inner, fg_color="transparent")
        frame_data_inicial.pack(fill="x", pady=2)
        ctk.CTkLabel(frame_data_inicial, text="De (Data Inicial):", text_color=self.text_color, width=120, anchor="w").pack(side="left", padx=(0,10))
        self.entrada_data_inicial = DateEntry(frame_data_inicial, date_pattern="dd/mm/yyyy", width=15,
                                              background=self.cyber_fg_color, foreground=self.text_color, 
                                              borderwidth=2, selectbackground=self.button_color, headersbackground=self.button_color)
        self.entrada_data_inicial.pack(side="left")

        frame_data_final = ctk.CTkFrame(date_frame_inner, fg_color="transparent")
        frame_data_final.pack(fill="x", pady=2)
        ctk.CTkLabel(frame_data_final, text="Até (Data Final):", text_color=self.text_color, width=120, anchor="w").pack(side="left", padx=(0,10))
        self.entrada_data_final = DateEntry(frame_data_final, date_pattern="dd/mm/yyyy", width=15,
                                            background=self.cyber_fg_color, foreground=self.text_color, 
                                            borderwidth=2, selectbackground=self.button_color, headersbackground=self.button_color)
        self.entrada_data_final.pack(side="left")
        self.entrada_data_final.set_date(datetime.now())

        formats_frame_outer = ctk.CTkFrame(content_frame, fg_color=self.cyber_fg_color, corner_radius=10)
        formats_frame_outer.pack(pady=10, padx=10, fill="x")
        ctk.CTkLabel(formats_frame_outer, text="Selecione os formatos a deletar:", text_color=self.label_header_color, font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=(5,5), padx=10)

        checkbox_options = {
            "text_color": self.text_color,
            "fg_color": self.checkbox_color,
            "hover_color": self.button_hover_color,
            "checkmark_color": "#000000"
        }
        
        checkbox_grid = ctk.CTkFrame(formats_frame_outer, fg_color="transparent")
        checkbox_grid.pack(fill="x", padx=10, pady=5)
        
        for i in range(3): 
            checkbox_grid.columnconfigure(i, weight=1)

        checkboxes_data = [
            (".xlsx (Excel)", self.var_xlsx, 0, 0), (".docx (Word)", self.var_docx, 0, 1), (".pdf (PDF)", self.var_pdf, 0, 2),
            (".xml (XML)", self.var_xml, 1, 0), (".zip (ZIP)", self.var_zip, 1, 1), (".ogg (OGG)", self.var_ogg, 1, 2),
            (".png (PNG)", self.var_png, 2, 0), (".jpeg (JPEG)", self.var_jpeg, 2, 1), (".py (Python)", self.var_py, 2, 2),
            (".exe (EXE)", self.var_exe, 3, 0), (".pyw (PyWin)", self.var_pyw, 3, 1)
        ]

        for text, var, r, c in checkboxes_data:
            cb = ctk.CTkCheckBox(checkbox_grid, text=text, variable=var, **checkbox_options)
            cb.grid(row=r, column=c, sticky="w", padx=5, pady=3)

        exception_frame_outer = ctk.CTkFrame(content_frame, fg_color=self.cyber_fg_color, corner_radius=10)
        exception_frame_outer.pack(pady=10, padx=10, fill="x")
        
        exception_frame_inner = ctk.CTkFrame(exception_frame_outer, fg_color="transparent")
        exception_frame_inner.pack(pady=5, padx=10, fill="x")

        ctk.CTkLabel(exception_frame_inner, text="Exceção de Palavra (opcional):", text_color=self.text_color).pack(side="left", padx=(0,10))
        self.entrada_palavra_excecao = ctk.CTkEntry(exception_frame_inner, width=200, text_color=self.entry_text_color, fg_color="#1A1A1A", border_color=self.button_color)
        self.entrada_palavra_excecao.pack(side="left", expand=True, fill="x")

        footer_frame = ctk.CTkFrame(self, fg_color=self.amoled_black) 
        footer_frame.pack(side="bottom", fill="x", padx=20, pady=(10,20))

        self.progress_label = ctk.CTkLabel(footer_frame, text="Progresso: 0%", text_color=self.progress_text_color, font=ctk.CTkFont(size=12))
        
        self.progressbar = ctk.CTkProgressBar(footer_frame, orientation="horizontal", progress_color=self.progress_bar_color)
        self.progressbar.set(0) 
        
        self.delete_button = ctk.CTkButton(footer_frame, text="DELETAR ARQUIVOS SELECIONADOS", command=self.deletar_arquivos,
                                           fg_color="#FF0000", hover_color="#B22222",
                                           text_color="#FFFFFF", font=ctk.CTkFont(size=14, weight="bold"),
                                           height=40)
        self.delete_button.pack(fill="x", padx=10, ipady=5, pady=(5,0))

        self._reset_progress_visibility(initial=True) # Ocultar inicialmente


    def selecionar_diretorio(self):
        caminho = filedialog.askdirectory()
        if caminho:
            self.entrada_diretorio.delete(0, ctk.END)
            self.entrada_diretorio.insert(0, caminho)

    def _reset_progress_visibility(self, initial=False):
        if not initial: 
            self.progress_label.pack_forget()
            self.progressbar.pack_forget()
        self.progress_label.configure(text="Progresso: 0%")
        self.progressbar.set(0)
        self.progressbar.configure(mode="determinate") 
        if hasattr(self, 'delete_button'): # Adiciona verificação para segurança
            self.delete_button.configure(state="normal")

    def _show_progress_elements(self):
        # Garante que o botão exista antes de tentar usar como referência para 'before'
        if hasattr(self, 'delete_button'):
            self.progress_label.pack(pady=(5,0), before=self.delete_button)
            self.progressbar.pack(fill="x", padx=10, pady=(0,10), before=self.delete_button)
        else: # Fallback se o botão ainda não estiver pronto (improvável neste fluxo)
            self.progress_label.pack(pady=(5,0))
            self.progressbar.pack(fill="x", padx=10, pady=(0,10))


    def deletar_arquivos(self):
        if hasattr(self, 'delete_button'):
            self.delete_button.configure(state="disabled")
        self._show_progress_elements()
        self.update_idletasks()

        try:
            diretorio = self.entrada_diretorio.get()
            if not diretorio or not os.path.isdir(diretorio):
                messagebox.showwarning("Atenção", "Por favor, selecione um diretório válido.")
                self._reset_progress_visibility()
                return

            try:
                data_inicial_str = self.entrada_data_inicial.get()
                data_final_str = self.entrada_data_final.get()
                if not data_inicial_str or not data_final_str:
                    messagebox.showwarning("Atenção", "Por favor, selecione as datas inicial e final.")
                    self._reset_progress_visibility()
                    return
                data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")
                data_final = datetime.strptime(data_final_str, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Erro de Data", "Formato de data inválido. Use DD/MM/AAAA.")
                self._reset_progress_visibility()
                return

            if data_inicial > data_final:
                messagebox.showwarning("Atenção", "A data inicial não pode ser posterior à data final.")
                self._reset_progress_visibility()
                return

            formatos_selecionados = []
            if self.var_xlsx.get(): formatos_selecionados.append(".xlsx")
            if self.var_docx.get(): formatos_selecionados.append(".docx")
            if self.var_pdf.get(): formatos_selecionados.append(".pdf")
            if self.var_xml.get(): formatos_selecionados.append(".xml")
            if self.var_zip.get(): formatos_selecionados.append(".zip")
            if self.var_ogg.get(): formatos_selecionados.append(".ogg")
            if self.var_png.get(): formatos_selecionados.append(".png")
            if self.var_jpeg.get(): formatos_selecionados.append(".jpeg")
            if self.var_py.get(): formatos_selecionados.append(".py")
            if self.var_exe.get(): formatos_selecionados.append(".exe")
            if self.var_pyw.get(): formatos_selecionados.append(".pyw")

            if not formatos_selecionados:
                messagebox.showwarning("Atenção", "Selecione pelo menos um formato de arquivo para deletar.")
                self._reset_progress_visibility()
                return

            palavra_excecao = self.entrada_palavra_excecao.get().lower()
            data_final_com_fim_do_dia = datetime.combine(data_final.date(), datetime.max.time())

            self.progress_label.configure(text="Analisando arquivos...")
            self.progressbar.configure(mode="indeterminate")
            self.progressbar.start()
            self.update_idletasks()

            files_to_delete_list = []
            for root, _, files in os.walk(diretorio, topdown=True): 
                for file in files:
                    caminho_arquivo = os.path.join(root, file)
                    try:
                        if not any(file.lower().endswith(f) for f in formatos_selecionados):
                            continue
                        
                        data_modificacao_ts = os.path.getmtime(caminho_arquivo)
                        data_modificacao = datetime.fromtimestamp(data_modificacao_ts)

                        if data_inicial <= data_modificacao <= data_final_com_fim_do_dia:
                            if palavra_excecao and palavra_excecao in file.lower():
                                continue
                            files_to_delete_list.append(caminho_arquivo)
                    except FileNotFoundError: 
                        print(f"Arquivo não encontrado durante análise: {caminho_arquivo}")
                        continue
                    except Exception as e_scan: 
                        print(f"Erro ao analisar arquivo {caminho_arquivo}: {e_scan}")
                        continue
            
            self.progressbar.stop()
            self.progressbar.configure(mode="determinate")
            total_files_to_process = len(files_to_delete_list)

            if total_files_to_process == 0:
                messagebox.showinfo("Nenhum Arquivo", "Nenhum arquivo encontrado correspondendo aos critérios para exclusão.")
                self._reset_progress_visibility()
                return

            confirmacao = messagebox.askyesno("Confirmar Exclusão", 
                                              f"Você está prestes a deletar {total_files_to_process} arquivo(s) no diretório:\n{diretorio}\n"
                                              f"Entre as datas: {data_inicial.strftime('%d/%m/%Y')} e {data_final.strftime('%d/%m/%Y')}.\n"
                                              "Esta ação é IRREVERSÍVEL. Deseja continuar?")
            if not confirmacao:
                self._reset_progress_visibility()
                return

            deleted_files_count = 0
            failed_to_delete_count = 0
            for i, caminho_arquivo in enumerate(files_to_delete_list):
                try:
                    os.remove(caminho_arquivo)
                    deleted_files_count += 1
                except Exception as e_file:
                    failed_to_delete_count +=1
                    print(f"Erro ao deletar o arquivo {caminho_arquivo}: {str(e_file)}")
                
                progress_percentage = (i + 1) / total_files_to_process
                self.progressbar.set(progress_percentage)
                self.progress_label.configure(text=f"Progresso: {int(progress_percentage * 100)}%")
                self.update_idletasks()

            msg_final = f"{deleted_files_count} de {total_files_to_process} arquivo(s) selecionado(s) foram deletados com sucesso."
            if failed_to_delete_count > 0:
                msg_final += f"\n{failed_to_delete_count} arquivo(s) não puderam ser deletados (verifique o console para erros)."
            messagebox.showinfo("Operação Concluída", msg_final)
        
        except FileNotFoundError: 
            messagebox.showerror("Erro", f"Diretório principal não encontrado: {diretorio}")
        except Exception as e:
            messagebox.showerror("Erro Crítico", f"Ocorreu um erro inesperado: {str(e)}")
        finally:
            self._reset_progress_visibility()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue") 
    
    app = App()
    app.mainloop()
