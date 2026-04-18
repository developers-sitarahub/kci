import type { Metadata } from "next";
import { Inter, Cardo } from "next/font/google";
import "./globals.css";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const cardo = Cardo({ weight: ["400", "700"], subsets: ["latin"], variable: "--font-cardo" });

export const metadata: Metadata = {
  title: "Kanji Capital Investments | Houston Commercial Real Estate",
  description: "Kanji Capital Investments — a family-owned commercial real estate firm based in Houston, Texas. Buying, selling, leasing, and investing since 2018.",
  icons: {
    icon: "/icon.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${cardo.variable} scroll-smooth`}>
      <body className="min-h-screen flex flex-col font-inter text-gray-900 bg-white antialiased">
        <Navbar />
        <div className="pt-[72px] flex flex-col flex-1">
          {children}
        </div>
        <Footer />
      </body>
    </html>
  );
}
