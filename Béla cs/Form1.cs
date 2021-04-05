using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Discord;

namespace Béla_cs
{
    public partial class Form1 : Form
    {

        public Point mouseLocation;
        Form2 form2 = new Form2();
        int m = 0;
        public Form1()
        {
            InitializeComponent();
            
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoginAsUserGuest.Enabled = false;
            label7.Hide();
            if (m == 1)
            {
                button3.Hide();
                panel2.Hide();
                label6.Hide();
            }
            if (m == 1)
            {
                label7.Show();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void form1_MouseDown(object sender, MouseEventArgs e)
        {
            mouseLocation = new Point(-e.X, -e.Y);
        }

        private void form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                Point mousePose = Control.MousePosition;
                mousePose.Offset(mouseLocation.X, mouseLocation.Y);
                Location = mousePose;
            }
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void form2nav_Click(object sender, EventArgs e)
        {
            this.Hide();
            var form2 = new Form2();
            form2.Closed += (s, args) => this.Close();
            form2.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {            
                button3.Hide();
                panel2.Hide();
                label6.Hide();
                m = 1;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text.ToString() == "guest")
            {
                LoginAsUserGuest.Enabled = true;
                
            }
            else
            {
                LoginAsUserGuest.Enabled = false;
            }
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
 
        }

        private void label7_Click(object sender, EventArgs e)
        {
        
        }

        private void LoginAsUserGuest_Click(object sender, EventArgs e)
        {
            this.Hide();
            var form3 = new Form3();
            form3.Closed += (s, args) => this.Close();
            form3.Show();
        }

        static void UpdatePresence()
        {
            DiscordRichPresence discordPresence;
            memset(&discordPresence, 0, sizeof(discordPresence));
            discordPresence.state = "Béla egyre okosabb lesz";
            discordPresence.details = "Béla: DevVersion 1";
            discordPresence.partyId = " ";
            Discord_UpdatePresence(&discordPresence);
        }
    }
}
